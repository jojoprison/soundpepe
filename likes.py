import os
import re
import subprocess


def download_recent_tracks(user_url, num_tracks=33):
    try:
        # Fetch the username from the URL
        print(f"Extracting username from URL: {user_url}")
        username = user_url.rstrip('/').split('/')[-1]
        print(f"Username extracted: {username}")

        # Create a directory for the user if it doesn't exist
        if not os.path.exists(username):
            print(f"Creating directory for user: {username}")
            os.makedirs(username)
        else:
            print(f"Directory already exists for user: {username}")

        # Build the scdl command to fetch liked tracks
        archive_file = os.path.join(username, "downloaded_liked_tracks.txt")

        # Fast path: не делаем сетевые запросы перед стартом.
        # Создадим файл архива, если его нет (scdl сам будет его пополнять для новых треков).
        os.makedirs(username, exist_ok=True)
        if not os.path.exists(archive_file):
            try:
                with open(archive_file, "a", encoding="utf-8"):
                    pass
            except OSError:
                pass
        command = [
            "scdl",
            "-l", user_url,
            "-f",  # likes (favorites)
            "-c",  # continue if file exists (skip by filename)
            "--onlymp3",  # force mp3 output
            "--no-original",  # avoid downloading original files like m4a
            "--download-archive", archive_file,  # skip already-downloaded by track id
            "--path", username,  # saving directory
            # "--name-format", "%(title)s"  # by default format is sc track ID
        ]

        print(f"Constructed scdl command: {' '.join(command)}")
        # Pre-run counts
        before_mp3 = sum(1 for f in os.listdir(username) if
                         f.lower().endswith(".mp3")) if os.path.exists(
            username) else 0
        before_archive = 0
        if os.path.exists(archive_file):
            try:
                with open(archive_file, "r", encoding="utf-8") as af:
                    before_archive = sum(1 for _ in af)
            except OSError:
                before_archive = 0

        # Patterns for parsing scdl logs
        like_total = None
        new_downloads = 0
        skipped_existing = 0

        pat_like_total = re.compile(r"like n°(\d+) of (\d+)")
        pat_downloading = re.compile(r"Downloading (.+)")
        pat_downloaded = re.compile(r"(.+) Downloaded\.")
        pat_skipped = re.compile(r"(.+) already downloaded\.")

        # Run the scdl command (stream logs)
        print("Running scdl command...")
        env = dict(os.environ)
        env["PYTHONUNBUFFERED"] = "1"
        with subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1,
                env=env,
        ) as proc:
            try:
                assert proc.stdout is not None
                for line in proc.stdout:
                    line = line.strip()
                    if not line:
                        continue

                    m_tot = pat_like_total.search(line)
                    if m_tot and like_total is None:
                        like_total = int(m_tot.group(2))
                        print(f"Всего лайков у пользователя: {like_total}")

                    m_dl = pat_downloading.search(line)
                    if m_dl:
                        current_title = m_dl.group(1)
                        print(
                            f"Скачиваю: {current_title} (новых {new_downloads}/{num_tracks})")

                    if pat_skipped.search(line):
                        skipped_existing += 1

                    if pat_downloaded.search(line):
                        new_downloads += 1
                        print(f"Готово: {new_downloads}/{num_tracks}")

                    # Stop after reaching requested number of new downloads
                    if num_tracks and new_downloads >= int(num_tracks):
                        print("Достигнут лимит новых загрузок. Останавливаю...")
                        proc.terminate()
                        break
            finally:
                try:
                    proc.wait(timeout=10)
                except Exception:
                    pass

        # Post-run counts and summary
        after_mp3 = sum(1 for f in os.listdir(username) if
                        f.lower().endswith(".mp3")) if os.path.exists(
            username) else 0
        after_archive = before_archive
        if os.path.exists(archive_file):
            try:
                with open(archive_file, "r", encoding="utf-8") as af:
                    after_archive = sum(1 for _ in af)
            except OSError:
                pass

        added_by_archive = max(0, after_archive - before_archive)
        added_by_files = max(0, after_mp3 - before_mp3)

        print("\n=== Итог ===")
        if like_total is not None:
            print(f"Всего лайков у пользователя: {like_total}")
        print(f"Запрошено к скачиванию (лимит новых): {num_tracks}")
        print(f"Новых скачано (по логам): {new_downloads}")
        print(f"Новых в архиве: {added_by_archive}")
        print(f"Новых .mp3 файлов: {added_by_files}")
        print(f"Пропущено (уже были): {skipped_existing}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # URL of the user's profile
    user_profile_url = "https://soundcloud.com/up_to_u"
    download_recent_tracks(user_profile_url, num_tracks=299)

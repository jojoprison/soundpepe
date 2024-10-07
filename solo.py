import subprocess
import os


def download_track_by_link(track_url):
    try:
        # Fetch the track ID or title from the URL
        track_id = track_url.rstrip('/').split('/')[-1]
        print(f"Track ID extracted: {track_id}")

        dir_name = 'jkaseq'

        # Create a directory for the track if it doesn't exist
        if not os.path.exists(dir_name):
            print("Creating 'tracks' directory")
            os.makedirs(dir_name)
        else:
            print("'tracks' directory already exists")

        # Build the scdl command to download the track
        command = [
            "scdl",
            "-l", track_url,
            "--path", dir_name,  # saving directory
        ]

        print(f"Constructed scdl command: {' '.join(command)}")

        # Run the scdl command
        print("Running scdl command...")
        result = subprocess.run(command, capture_output=True, text=True)
        print("scdl command finished running")

        # Check if the command was successful
        if result.returncode == 0:
            print(f"Successfully downloaded track from {track_url}")
        else:
            print(f"Failed to download track. Error: {result.stderr}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    track_url = '''

https://soundcloud.com/beatstars/yeat-x-sofayo-type-beat-rage-hyperpop-instrumental-atari?si=f80f8a5ad3694e7e83d840e79439370b&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

'''
    track_url = track_url.strip()
    download_track_by_link(track_url)

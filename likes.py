import subprocess
import os


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
        command = [
            "scdl",
            "-l", user_url,
            "-f",  # likes (favorites)
            "-n", str(num_tracks),
            # "--download-archive", os.path.join(username, "downloaded_liked_tracks.txt"),
            "--path", username,  # saving directory
            # "--name-format", "%(title)s"  # by default format is sc track ID
        ]

        print(f"Constructed scdl command: {' '.join(command)}")

        # Run the scdl command
        print("Running scdl command...")
        result = subprocess.run(command, capture_output=True, text=True)
        print("scdl command finished running")

        # Check if the command was successful
        if result.returncode == 0:
            print(f"Successfully downloaded up to {num_tracks} liked tracks from {user_url}")
        else:
            print(f"Failed to download liked tracks. Error: {result.stderr}")

    except Exception as e:
        print(f"An error occurred: {e}")




if __name__ == "__main__":
    # URL of the user's profile
    user_profile_url = "https://soundcloud.com/supadupafla"
    download_recent_tracks(user_profile_url, num_tracks=33)

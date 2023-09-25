import os
from pytube import YouTube

# Get the YouTube video URL from the user
video_url = input("Enter the YouTube video URL: ")

# Folder where you want to save the downloaded video
output_folder = r"<your download folder>"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Initialize a YouTube object
yt = YouTube(video_url)

# Get the highest quality stream
stream = yt.streams.get_highest_resolution()

# Download the video to the specified folder
print(f"Downloading {yt.title}...")
stream.download(output_path=output_folder)

print("Download complete!")

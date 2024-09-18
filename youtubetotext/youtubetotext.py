import os
import glob
import re
import urllib.parse
from pytube import YouTube


# Function to clean the video title for a valid filename
def clean_filename(title):
    # Remove special characters using regex, only allow alphanumeric, dashes, and underscores
    return re.sub(r"[^A-Za-z0-9_\- ]+", "", title)


# 1. Enter a URL for a YouTube video
url = input("Enter the YouTube video URL: ")

# Access the YouTube video using pytube
yt = YouTube(url)

# Get the title of the video
video_title = yt.title

# Get the channel name
channel_name = yt.author

# Clean the video title for file saving
cleaned_title = clean_filename(video_title)
cleaned_channel_name = clean_filename(channel_name)

yt = YouTube(url)

# Extract a safe filename from the URL by getting the video ID
def extract_video_id(url):
    # Parse URL to get query parameters
    parsed_url = urllib.parse.urlparse(url)
    if "youtube" in parsed_url.netloc:
        query = urllib.parse.parse_qs(parsed_url.query)
        video_id = query.get("v")
        if video_id:
            return video_id[0]
    elif "youtu.be" in parsed_url.netloc:
        return parsed_url.path.strip("/")
    else:
        return None


video_id = extract_video_id(url)
if not video_id:
    print("Could not extract video ID from the URL.")
    exit()

# Sanitize video_id to create a valid filename
filename_base = re.sub(r"[^\w\-_. ]", "_", video_id)

# 2. Download the video with yt-dlp
print("Downloading video...")
from yt_dlp import YoutubeDL

ydl_opts = {"format": "bestvideo+bestaudio/best", "outtmpl": f"{filename_base}.%(ext)s"}

with YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

# Find the downloaded video file
video_files = glob.glob(f"{filename_base}.*")
if len(video_files) == 0:
    print("No video file downloaded.")
    exit()
else:
    video_file = video_files[0]
    print(f"Video downloaded as {video_file}")

# 3. Split the audio and video from the downloaded video file
print("Extracting audio from video...")
from moviepy.editor import VideoFileClip

video = VideoFileClip(video_file)
audio = video.audio
audio_file = f"{filename_base}_audio.wav"
audio.write_audiofile(audio_file)
video.close()  # Close the video file to free resources

# 4. Transcribe the video audio to a text file with Whisper
print("Transcribing audio with Whisper...")
import whisper

model = whisper.load_model("base")  # Options: 'tiny', 'small', 'medium', 'large'
result = model.transcribe(audio_file)
transcription = result["text"]

# transcription_file = f"{filename_base}_transcription.txt"
transcription_file = f"{cleaned_channel_name} - {cleaned_title}_transcription.txt"
with open(transcription_file, "w", encoding="utf-8") as f:
    f.write(transcription)

print(f"Transcription saved to {transcription_file}")

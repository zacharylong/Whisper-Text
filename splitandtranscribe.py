import os
from moviepy.editor import VideoFileClip
import whisper

# Step 1: Store the long path separately (dynamic input file)
video_file_path = "/Users/zacharylong/Library/CloudStorage/Dropbox/NYU MSBA/Module 1/Intro to BA/Course Recordings/XBA1-GB-8336-84S23512023-01.mp4"

# Step 2: Extract the base file name (without path and extension)
base_name = os.path.splitext(os.path.basename(video_file_path))[0]

# Step 3: Extract audio from the video file and save it as a .wav file
video = VideoFileClip(video_file_path)
audio_file = f"{base_name}.wav"
video.audio.write_audiofile(audio_file)
video.close()

# Step 4: Load Whisper model and transcribe the audio
model = whisper.load_model("base")
result = model.transcribe(audio_file)

# Step 5: Save the transcribed text to a .txt file with the same base name
transcribed_text_file = f"{base_name}.txt"
with open(transcribed_text_file, "w") as f:
    f.write(result["text"])

# Optionally, print the saved file path
print(f"Transcription saved to: {transcribed_text_file}")

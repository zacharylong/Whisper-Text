import os
from moviepy.editor import VideoFileClip
import whisper

# Step 1: Define the directory containing the video files
video_directory = "/Users/zacharylong/dwhelper"

# Step 2: Load the Whisper model
model = whisper.load_model("base")

# Step 3: Loop through all video files in the directory
for file_name in os.listdir(video_directory):
    if file_name.endswith(".mp4"):  # Only process .mp4 files
        # Get the full path to the video file
        video_file_path = os.path.join(video_directory, file_name)

        # Extract the base file name (without path and extension)
        base_name = os.path.splitext(file_name)[0]

        # Step 4: Extract audio from the video file
        video = VideoFileClip(video_file_path)
        audio_file = f"{base_name}.wav"
        video.audio.write_audiofile(audio_file)
        video.close()

        # Step 5: Transcribe the audio using Whisper
        result = model.transcribe(audio_file)

        # Step 6: Save the transcribed text to a .txt file
        transcribed_text_file = f"{base_name}.txt"
        with open(transcribed_text_file, "w") as f:
            f.write(result["text"])

        # Step 7: Delete the generated audio .wav file
        os.remove(audio_file)

        # Output confirmation message
        print(f"Transcription for {file_name} saved as {transcribed_text_file}.")
        print(f"Temporary audio file {audio_file} deleted.")

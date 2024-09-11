from moviepy.editor import VideoFileClip

# Path to your video file
video_file = "/Users/zacharylong/Library/CloudStorage/Dropbox/NYU MSBA/Module 1/Intro to BA/Course Recordings/XBA1-GB-8336-84S23512023.mp4"

# Load the video file
video = VideoFileClip(video_file)

# Extract the audio
audio = video.audio

# Save the extracted audio to a .wav file
audio_file = "XBA1-GB-8336-84S23512023_extracted_audio.wav"
audio.write_audiofile(audio_file)

# Close the video clip
video.close()

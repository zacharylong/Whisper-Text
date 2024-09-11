import whisper

# Load Whisper model (you can use different model sizes, e.g., 'base', 'small', 'medium', 'large')
model = whisper.load_model("base")

# Transcribe the audio file
result = model.transcribe(
    "/Users/zacharylong/Library/CloudStorage/Dropbox/NYU MSBA/Module 1/Intro to BA/Course Recordings/XBA1-GB-8336-84S23512023_extracted_audio.wav"
)

# Print the transcribed text
print(result["text"])

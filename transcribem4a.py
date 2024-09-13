import whisper
import sys
import os


def main():
    if len(sys.argv) != 2:
        print("Usage: python transcribe.py audio_file.m4a")
        sys.exit(1)

    audio_file = sys.argv[1]

    if not os.path.isfile(audio_file):
        print(f"File not found: {audio_file}")
        sys.exit(1)

    # Load the Whisper model (choose 'tiny', 'base', 'small', 'medium', or 'large')
    model = whisper.load_model("base")

    # Transcribe the audio file
    print("Transcribing audio...")
    result = model.transcribe(audio_file)

    # Get the transcription text
    transcription = result["text"]

    # Save the transcription to a text file
    output_file = os.path.splitext(audio_file)[0] + ".txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(transcription)

    print(f"Transcription saved to {output_file}")


if __name__ == "__main__":
    main()

"""
Usage:
python transcribem4a.py audio_file.m4a

"""

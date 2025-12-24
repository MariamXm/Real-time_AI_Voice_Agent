import sounddevice as sd
import soundfile as sf
import librosa
import whisper

SAMPLE_RATE = 16000
AUDIO_FILE = "input.wav"

# Load Whisper model
model = whisper.load_model("base")

def record_audio(duration=5, filename=AUDIO_FILE):
    print("🎙️ Recording...")
    audio = sd.rec(int(duration * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1)
    sd.wait()
    sf.write(filename, audio, SAMPLE_RATE)
    print(f" Saved audio to {filename}")
    return filename

def transcribe_audio(file_path):
    audio, sr = librosa.load(file_path, sr=16000)
    result = model.transcribe(audio)
    return result["text"]

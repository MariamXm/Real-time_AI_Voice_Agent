import os
import streamlit as st
import sounddevice as sd
import soundfile as sf
import librosa
import whisper
from llm.agent import get_groq_response  # Groq AI wrapper
from tts.speaker import speak_text  # Import TTS from speaker.py


from streamlit_webrtc import webrtc_streamer, AudioProcessorBase, WebRtcMode
import numpy as np

class AudioProcessor(AudioProcessorBase):
    def recv_audio(self, frame):
        audio_data = frame.to_ndarray()
        # Save or process audio_data here
        return frame

webrtc_streamer(
    key="microphone",
    mode=WebRtcMode.SENDRECV,
    audio_processor_factory=AudioProcessor
)

# ----------------------------- CONFIG
SAMPLE_RATE = 16000
DURATION = 5
AUDIO_FILE = "input.wav"
OUTPUT_AUDIO = "response.wav"

# Load Whisper model
model = whisper.load_model("base")

# ----------------------------- AUDIO RECORDING
def record_audio(duration=DURATION, filename=AUDIO_FILE):
    st.info(" Recording your voice...")
    audio = sd.rec(int(duration * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1)
    sd.wait()
    sf.write(filename, audio, SAMPLE_RATE)
    st.success(f" Audio saved as {filename}")
    return filename

# ----------------------------- TRANSCRIBE
def transcribe_audio(file_path):
    audio, sr = librosa.load(file_path, sr=16000)
    result = model.transcribe(audio)
    return result["text"]

# ----------------------------- STREAMLIT UI
st.set_page_config(page_title="Real-Time Voice AI Agent", layout="centered")
st.title(" Real-Time Voice AI Agent")


if st.button(" Record & Generate Response"):
    # Record audio
    wav_file = record_audio()

    # Transcribe
    user_text = transcribe_audio(wav_file)
    st.subheader("You said:")
    st.text_area("", user_text, height=80)

    # Get AI response
    ai_response = get_groq_response(user_text)
    st.subheader("AI Response:")
    st.text_area("", ai_response, height=350)

    # Generate TTS
    speak_text(ai_response, filename=OUTPUT_AUDIO)

    # Add audio player
    st.audio(OUTPUT_AUDIO)



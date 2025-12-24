import streamlit as st
import whisper
import librosa
import asyncio
from llm.agent import get_groq_response
from tts.speaker import speak_text

st.set_page_config(page_title="Voice AI Agent", layout="centered")

model = whisper.load_model("base")
OUTPUT_AUDIO = "response.wav"

#UI
st.title(" Voice AI Agent")
st.write("Click **Record**, speak, then wait for the AI response.")

# RECORD AUDIO (BROWSER MIC)
audio_input = st.audio_input(" Record your voice")

if audio_input is not None:
    # Save recorded audio
    with open("input.wav", "wb") as f:
        f.write(audio_input.read())

    st.success(" Audio recorded")

    # TRANSCRIBE
    st.info(" Transcribing audio...")
    audio, _ = librosa.load("input.wav", sr=16000)
    result = model.transcribe(audio, fp16=False)
    user_text = result["text"].strip()

    st.subheader(" You said:")
    st.text_area("", user_text, height=80)

    #  AI RESPONSE
    st.info(" Generating AI response...")
    ai_response = get_groq_response(user_text)

    st.subheader("AI Response:")
    st.text_area("", ai_response, height=450)

    # TEXT TO SPEECH
    st.info(" Generating voice...")
    asyncio.run(speak_text(ai_response, filename=OUTPUT_AUDIO))

    st.subheader("AI Voice Response:")
    st.audio(OUTPUT_AUDIO)

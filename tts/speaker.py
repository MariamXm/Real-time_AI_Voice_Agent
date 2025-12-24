# speaker.py
import edge_tts
import asyncio

async def generate_tts(text, voice="en-US-GuyNeural", filename="response.wav"):
    """
    Converts text to speech and saves as WAV.
    Removes unnecessary line breaks or separators.
    """
    # Clean text: remove extra = signs, long dashes, multiple newlines
    clean_text = text.replace("=", "").replace("\n", " ").strip()
    communicate = edge_tts.Communicate(clean_text, voice)
    await communicate.save(filename)

def speak_text(text, filename="response.wav"):
    asyncio.run(generate_tts(text, filename=filename))

# speaker.py
# import edge_tts
# import asyncio

# async def generate_tts(text, voice="en-US-GuyNeural", filename="response.wav"):
#     """
#     Converts text to speech and saves as WAV.
#     Removes unnecessary line breaks or separators.
#     """
#     # Clean text: remove extra = signs, long dashes, multiple newlines
#     clean_text = text.replace("=", "").replace("\n", " ").strip()
#     communicate = edge_tts.Communicate(clean_text, voice)
#     await communicate.save(filename)

# def speak_text(text, filename="response.wav"):
#     asyncio.run(generate_tts(text, filename=filename))

import edge_tts
import asyncio

async def generate_tts(text, voice="en-US-GuyNeural", filename="response.wav"):
    """
    Converts text to speech and saves as WAV.
    Cleans unnecessary characters for natural speech.
    """
    clean_text = text.replace("=", "").replace("\n", " ").strip()
    communicate = edge_tts.Communicate(clean_text, voice)
    await communicate.save(filename)

# Make speak_text an async function
async def speak_text(text, filename="response.wav"):
    await generate_tts(text, filename=filename)


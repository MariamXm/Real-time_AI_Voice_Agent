from asr.transcriber import record_audio, transcribe_audio
from tts.speaker import speak_text
from llm.agent import get_groq_response
import asyncio


if __name__ == "__main__":
    try:
        # Record user audio
        wav_file = record_audio()

        # Transcribe audio
        user_text = transcribe_audio(wav_file)
        print("You said:", user_text)

        # Get AI response
        ai_response = get_groq_response(user_text)
        print("AI:", ai_response)

        # Convert AI response to speech
        asyncio.run(speak_text(ai_response))

    except Exception as e:
        print("Error:", e)

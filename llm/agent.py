import os
from dotenv import load_dotenv  # Import dotenv
from groq import Groq

# Load variables from .env file
load_dotenv()  # This looks for a .env file in the project root

# Get the API key from environment variables
api_key = os.environ.get("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY not set in environment")

# Initialize Groq client
client = Groq(api_key=api_key)

def get_groq_response(prompt):
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        model="llama-3.3-70b-versatile",
        max_tokens=650
    )
    return chat_completion.choices[0].message.content


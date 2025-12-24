# import os
# from dotenv import load_dotenv
# from groq import Groq

# load_dotenv()

# client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# def get_groq_response(prompt):
#     chat_completion = client.chat.completions.create(
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": prompt},
#         ],
#         model="llama-3.3-70b-versatile",
#         max_tokens=520
#     )
#     return chat_completion.choices[0].message.content

import os
from groq import Groq

# Use environment variable directly, safer in deployment
api_key = os.environ.get("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY not set in environment")

client = Groq(api_key=api_key)

def get_groq_response(prompt):
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        model="llama-3.3-70b-versatile",
        max_tokens=520
    )
    return chat_completion.choices[0].message.content


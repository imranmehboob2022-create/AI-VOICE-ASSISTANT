import os
from groq import Groq
from dotenv import load_dotenv

# Load the .env file from Desktop
load_dotenv(r"C:\Users\Imran\Desktop\.env")

# Read the API key
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found in C:\\Users\\Imran\\Desktop\\.env")

# Create Groq client
client = Groq(api_key=api_key)


def ask_ai(prompt):
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful AI assistant."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7,
            max_tokens=1024
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {e}"
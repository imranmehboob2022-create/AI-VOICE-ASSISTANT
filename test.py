from groq import Groq

# Replace with your actual API key
client = Groq(api_key="gsk_your_actual_api_key")

try:
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": "Say Hello!"
            }
        ]
    )

    print("✅ API Key is working!")
    print(response.choices[0].message.content)

except Exception as e:
    print("❌ Error:")
    print(e)
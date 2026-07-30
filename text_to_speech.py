import os
import uuid
import edge_tts

VOICE = "en-US-AriaNeural"

# Hindi:
# VOICE = "hi-IN-SwaraNeural"

# Urdu:
# VOICE = "ur-PK-UzmaNeural"


def speak(text):
    """
    Generate speech audio using Edge TTS.
    Returns the generated MP3 file path.
    """

    text = str(text).strip()

    if not text:
        return None

    # Create audio folder inside static
    audio_folder = os.path.join("static", "audio")
    os.makedirs(audio_folder, exist_ok=True)

    # Unique filename for every response
    filename = f"{uuid.uuid4().hex}.mp3"
    file_path = os.path.join(audio_folder, filename)

    async def generate():
        communicate = edge_tts.Communicate(text, VOICE)
        await communicate.save(file_path)

    import asyncio
    asyncio.run(generate())

    return file_path
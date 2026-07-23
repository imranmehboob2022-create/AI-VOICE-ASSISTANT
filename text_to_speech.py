import asyncio
import os
import tempfile
import edge_tts
import pygame

pygame.mixer.init()

VOICE = "en-US-AriaNeural"   # Female voice
# Hindi: "hi-IN-SwaraNeural"
# Urdu: "ur-PK-UzmaNeural"


async def _speak(text):
    temp_file = os.path.join(tempfile.gettempdir(), "voice.mp3")

    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(temp_file)

    pygame.mixer.music.load(temp_file)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        await asyncio.sleep(0.1)

    pygame.mixer.music.unload()

    try:
        os.remove(temp_file)
    except:
        pass


def speak(text):
    asyncio.run(_speak(str(text)))
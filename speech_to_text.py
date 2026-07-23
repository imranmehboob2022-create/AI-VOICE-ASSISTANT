import pyttsx3
import threading


def speak(text):
    def run():
        engine = pyttsx3.init()

        voices = engine.getProperty("voices")

        if len(voices) > 1:
            engine.setProperty("voice", voices[1].id)
        else:
            engine.setProperty("voice", voices[0].id)

        engine.setProperty("rate", 170)
        engine.setProperty("volume", 1.0)

        engine.say(str(text))
        engine.runAndWait()
        engine.stop()

    thread = threading.Thread(target=run)
    thread.start()
    thread.join()
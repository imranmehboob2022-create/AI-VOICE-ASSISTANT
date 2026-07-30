
from flask import Flask, render_template, request, jsonify, url_for

from llm import ask_ai
from text_to_speech import speak

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    message = data.get("message", "").strip()

    if not message:
        return jsonify({
            "error": "Message is required"
        }), 400

    try:
        # Get AI response
        reply = ask_ai(message)

        # Generate MP3 using Edge TTS
        audio_file = speak(reply)

        # Create browser-accessible URL
        audio_url = None

        if audio_file:
            # Convert:
            # static/audio/abc.mp3
            # into:
            # /static/audio/abc.mp3
            relative_path = audio_file.replace("\\", "/")

            if relative_path.startswith("static/"):
                relative_path = relative_path[7:]

            audio_url = url_for(
                "static",
                filename=relative_path
            )

        return jsonify({
            "reply": reply,
            "audio_url": audio_url
        })

    except Exception as e:
        print("ERROR:", e)

        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)
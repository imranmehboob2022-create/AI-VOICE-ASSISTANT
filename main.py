from flask import Flask, render_template, request, jsonify
from threading import Thread

from llm import ask_ai
from text_to_speech import speak

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    message = data.get("message", "")

    reply = ask_ai(message)

    Thread(target=speak, args=(reply,), daemon=True).start()

    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True)
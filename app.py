from flask import Flask, render_template, request, session, redirect
import openai
import os
from dotenv import load_dotenv

#new imports
import speech_recognition as sr
from gtts import gTTS

load_dotenv()

app = Flask(__name__)
app.secret_key = "your-secret-key"
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=["GET", "POST"])
def home():
    # Initialize conversation history once per session
    if "history" not in session:
        session["history"] = [
            {
                "role": "system",
                "content": "You are a helpful and friendly AI assistant. You remember the full context of the conversation and respond accordingly, offering follow-up responses when needed."
            },
            {
                "role": "assistant",
                "content": "👋 Hello! How can I assist you today?"
            }
        ]
        session["show_welcome"] = True

    user_input = None
    response = None

    if request.method == "POST":
        # Handling audio upload for speech-to-text
        if 'audio' in request.files and request.files['audio'].filename != '':
            audio_file = request.files['audio']
            recognizer = sr.Recognizer()
            audio_path = "temp_audio.wav"
            audio_file.save(audio_path)

            with sr.AudioFile(audio_path) as source:
                audio_data = recognizer.record(source)
                try:
                    user_input = recognizer.recognize_google(audio_data)
                except Exception as e:
                    user_input = f"[Speech recognition error: {e}]"

            os.remove(audio_path)
        else:
            preset = request.form.get("preset")
            if preset == "game":
                user_input = "Can you recommend me a video game?"
            elif preset == "movie":
                user_input = "Can you recommend me a movie?"
            elif preset == "book":
                user_input = "Can you recommend me a good book?"
            elif preset == "advice":
                user_input = "Can you give me some life advice?"
            else:
                user_input = request.form.get("user_input")

        session["history"].append({"role": "user", "content": user_input})

        try:
            completion = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=session["history"]
            )
            response = completion.choices[0].message.content.strip()
            session["history"].append({"role": "assistant", "content": response})

            # Text-to-speech generation
            tts = gTTS(response, lang='en')
            audio_response_path = "static/audio_response.mp3"
            tts.save(audio_response_path)

        except Exception as e:
            response = f"Error: {e}"
            session["history"].append({"role": "assistant", "content": response})

        session["show_welcome"] = False

    return render_template("index.html", 
                           response=response, 
                           user_input=user_input, 
                           history=session["history"], 
                           show_welcome=session.get("show_welcome", False))


@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

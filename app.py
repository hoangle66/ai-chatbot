from flask import Flask, render_template, request, session, redirect
from flask_session import Session
import openai
import os
from dotenv import load_dotenv

#imports for image attachment
import base64
from io import BytesIO
from PIL import Image

#Sql imports for History Chats
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# new imports for speech to text
import speech_recognition as sr
from gtts import gTTS

load_dotenv()

app = Flask(__name__)
app.secret_key = "your-secret-key"
openai.api_key = os.getenv("OPENAI_API_KEY")

# Database config
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///chat_history.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Re-add the ChatMessage model
class ChatMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(64), default="default_user")
    role = db.Column(db.String(10))  # 'user' or 'assistant'
    content = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

# Store session data on the server-side (in the filesystem)
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_FILE_DIR"] = "./flask_session"
app.config["SESSION_FILE_THRESHOLD"] = 500

Session(app)

@app.route("/", methods=["GET", "POST"])
def home():
    if "history" not in session:
        session["history"] = [
            {"role": "system", "content": "You are a helpful and friendly AI assistant."},
            {"role": "assistant", "content": "👋 Hello! How can I assist you today?"}
        ]
        session["show_welcome"] = True

    user_input = None
    response = None
    image_data = None
    image_html = None

    if request.method == "POST":
        # Handle audio input
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
            # Handle preset button
            preset = request.form.get("preset")
            if preset == "game":
                user_input = "Can you recommend me a video game?"
            elif preset == "movie":
                user_input = "Can you recommend me a movie?"
            elif preset == "book":
                user_input = "Can you recommend me a good book?"
            elif preset == "advice":
                user_input = "I need some advice, but first, can you ask me what kind of advice I need? For example: relationships, studying, or motivation?"
            elif preset == "travel":
                user_input = "Can you recommend me a good place to go travel?"
            elif preset == "food":
                user_input = "Can you recommend a recipe?"
            elif preset == "joke":
                user_input = "Tell me a joke"
            elif preset == "fun_fact":
                user_input = "Tell me a fun fact"
            elif preset == "music":
                user_input = "Can you recommend me a Song"
            elif preset == "history":
                user_input = "Can you give me a random fact in history"
            else:
                user_input = request.form.get("user_input")

        # Handle image upload
        if "image" in request.files:
            uploaded_image = request.files["image"]
            if uploaded_image and uploaded_image.filename != "":
                image = Image.open(uploaded_image.stream)
                buffered = BytesIO()
                image.save(buffered, format="PNG")
                image_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
                image_data = f"data:image/png;base64,{image_base64}"
                image_html = f'<img src="{image_data}" class="chat-image">'

        # Construct OpenAI message
        if image_data:
            user_message_for_openai = {
                "role": "user",
                "content": [
                    {"type": "text", "text": user_input},
                    {"type": "image_url", "image_url": {"url": image_data}}
                ]
            }
            display_msg = f"{image_html}<br>{user_input}"
            session["history"].append({"role": "user", "content": display_msg})
            db.session.add(ChatMessage(role="user", content=f"[Image] {user_input}"))
        else:
            user_message_for_openai = {"role": "user", "content": user_input}
            session["history"].append({"role": "user", "content": user_input})
            db.session.add(ChatMessage(role="user", content=user_input))

        # Prepare messages for OpenAI (sanitized)
        history_for_openai = []
        for msg in session["history"]:
            if msg["role"] in ("system", "assistant"):
                history_for_openai.append(msg)
            elif msg["role"] == "user":
                from bs4 import BeautifulSoup
                clean = BeautifulSoup(msg["content"], "html.parser").get_text()
                history_for_openai.append({"role": "user", "content": clean})
        history_for_openai.append(user_message_for_openai)

        try:
            completion = openai.chat.completions.create(
                model="gpt-4o",
                messages=history_for_openai
            )
            response = completion.choices[0].message.content.strip()
            session["history"].append({"role": "assistant", "content": response})
            db.session.add(ChatMessage(role="assistant", content=response))

            # Generate TTS audio
            tts = gTTS(response, lang='en')
            tts.save("static/audio_response.mp3")

        except Exception as e:
            response = f"Error: {e}"
            session["history"].append({"role": "assistant", "content": response})
            db.session.add(ChatMessage(role="assistant", content=response))

        db.session.commit()
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

# Route to show saved chat history
@app.route("/history")
def show_history():
    messages = ChatMessage.query.all()
    return render_template("history.html", messages=messages)

if __name__ == "__main__":
    app.run(debug=True)

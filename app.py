from flask import Flask, render_template, request, session, redirect
import openai
import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

load_dotenv()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///chat_history.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
class ChatMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(64), default="default_user")
    role = db.Column(db.String(10))  # 'user' or 'assistant'
    content = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
app.secret_key = "your-secret-key"
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=["GET", "POST"])
def home():
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

        # Save assistant greeting to the database
        db.session.add(ChatMessage(role="assistant", content="👋 Hello! How can I assist you today?"))
        db.session.commit()

    user_input = None
    response = None

    if request.method == "POST":
        # Handle preset buttons
        preset = request.form.get("preset")
        if preset == "game":
            user_input = "Can you recommend me a video game?"
        elif preset == "movie":
            user_input = "Can you recommend me a movie?"
        else:
            user_input = request.form["user_input"]

        session["history"].append({"role": "user", "content": user_input})

        # Save user message
        db.session.add(ChatMessage(role="user", content=user_input))

        try:
            completion = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=session["history"]
            )
            response = completion.choices[0].message.content.strip()
            session["history"].append({"role": "assistant", "content": response})

            # Save assistant response
            db.session.add(ChatMessage(role="assistant", content=response))

        except Exception as e:
            response = f"Error: {e}"
            session["history"].append({"role": "assistant", "content": response})
            db.session.add(ChatMessage(role="assistant", content=response))

        db.session.commit()
        session["show_welcome"] = False

    return render_template("index.html", response=response, user_input=user_input, history=session["history"], show_welcome=session.get("show_welcome", False))


@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")

@app.route("/history")
def show_history():
    messages = ChatMessage.query.all()
    return render_template("history.html", messages=messages)

if __name__ == "__main__":
    app.run(debug=True)


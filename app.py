from flask import Flask, render_template, request, session, redirect
import openai
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.secret_key = "your-secret-key"
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=["GET", "POST"])
def home():
    # Initialize conversation history once per session
    if "history" not in session or not session["history"]:
        session["history"] = [
            {"role": "system", "content": "You are a helpful chatbot."},
            {"role": "assistant", "content": "👋 Hello! How can I assist you today?"}
        ]

    user_input = None
    response = None

    if request.method == "POST":
        user_input = request.form["user_input"]
        session["history"].append({"role": "user", "content": user_input})

        try:
            completion = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=session["history"]
            )
            response = completion.choices[0].message.content.strip()
            session["history"].append({"role": "assistant", "content": response})

        except Exception as e:
            response = f"Error: {e}"
            session["history"].append({"role": "assistant", "content": response})

    return render_template("index.html", response=response, user_input=user_input, history=session["history"])

@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

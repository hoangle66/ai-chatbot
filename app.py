from flask import Flask, render_template, request, session, redirect
from flask_session import Session
import openai
import os
from dotenv import load_dotenv
import base64
from io import BytesIO
from PIL import Image

load_dotenv()
app = Flask(__name__)
app.secret_key = "your-secret-key"
openai.api_key = os.getenv("OPENAI_API_KEY")

# Store session data on the server-side (in the filesystem)
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_FILE_DIR"] = "./flask_session"  # Optional: choose a session folder
app.config["SESSION_FILE_THRESHOLD"] = 500  # Optional: how many session files before cleanup

Session(app)  # initialize Flask-Session extension

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
        # Get user input or preset
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
            user_input = request.form["user_input"]

        # Check for image
        if "image" in request.files:
            uploaded_image = request.files["image"]
            if uploaded_image and uploaded_image.filename != "":
                image = Image.open(uploaded_image.stream)
                buffered = BytesIO()
                image.save(buffered, format="PNG")
                image_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
                image_data = f"data:image/png;base64,{image_base64}"
                image_html = f'<img src="{image_data}" class="chat-image">'

        # Build OpenAI-compatible message
        if image_data:
            user_message_for_openai = {
                "role": "user",
                "content": [
                    {"type": "text", "text": user_input},
                    {"type": "image_url", "image_url": {"url": image_data}}
                ]
            }
            # Store display-safe version only
            session["history"].append({"role": "user", "content": f"{image_html}<br>{user_input}"})
        else:
            user_message_for_openai = {"role": "user", "content": user_input}
            session["history"].append({"role": "user", "content": user_input})

        # Build OpenAI history (exclude display HTML, sanitize it)
        history_for_openai = []
        for msg in session["history"]:
            if msg["role"] == "system" or msg["role"] == "assistant":
                history_for_openai.append(msg)
            elif msg["role"] == "user":
                from bs4 import BeautifulSoup
                clean = BeautifulSoup(msg["content"], "html.parser").get_text()
                history_for_openai.append({"role": "user", "content": clean})
        history_for_openai.append(user_message_for_openai)

        # Get assistant reply
        try:
            completion = openai.chat.completions.create(
                model="gpt-4o",
                messages=history_for_openai
            )
            response = completion.choices[0].message.content.strip()
        except Exception as e:
            response = f"Error: {e}"

        session["history"].append({"role": "assistant", "content": response})
        session["show_welcome"] = False

    return render_template("index.html", response=response, user_input=user_input,
                           history=session["history"], show_welcome=session.get("show_welcome", False))

@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)

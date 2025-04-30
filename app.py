from flask import Flask, render_template, request, session, redirect
import openai
import os
import base64
from io import BytesIO
from PIL import Image
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.secret_key = "your-secret-key"
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=["GET", "POST"])
def home():

    image_data = None
    display_html = None 

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

        # Check for uploaded image
        image_data = None
        if "image" in request.files:
            uploaded_image = request.files["image"]
            if uploaded_image.filename != "":
                image = Image.open(uploaded_image.stream)
                buffered = BytesIO()
                image.save(buffered, format="PNG")
                image_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
                image_data = f"data:image/png;base64,{image_base64}"
                # Save to session without image to avoid cookie overflow
                session["history"].append({"role": "user", "content": user_input})  # Only the text

        # Build message format
        if image_data:
            content = [
                {"type": "text", "text": user_input},
                {"type": "image_url", "image_url": {"url": image_data}}
            ]
        else:
            content = user_input

        # Save this just for display in the template, not in session
        display_html = f'<img src="{image_data}" class="chat-image">'

        

        try:
            completion = openai.chat.completions.create(
                model="gpt-4o",  # switch to GPT- versions
                messages=session["history"]
            )
            response = completion.choices[0].message.content.strip()
            session["history"].append({"role": "assistant", "content": response})
        except Exception as e:
            response = f"Error: {e}"
            session["history"].append({"role": "assistant", "content": response})

        session["show_welcome"] = False

    return render_template(
        "index.html",
        response=response,
        user_input=user_input,
        history=session["history"],
        show_welcome=session.get("show_welcome", False),
        display_image=display_html  # ✅ this stays
    )


@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

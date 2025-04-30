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

    # Initialize session history on first visit
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
        # Handle preset buttons
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

        # Handle image upload
        image_data = None
        if "image" in request.files:
            uploaded_image = request.files["image"]
            if uploaded_image and uploaded_image.filename != "":
                image = Image.open(uploaded_image.stream)
                buffered = BytesIO()
                image.save(buffered, format="PNG")
                image_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
                image_data = f"data:image/png;base64,{image_base64}"

        # Construct user message properly for GPT-4o
        if image_data:
            # Send to OpenAI, but only store a simplified version for display
            user_message_to_openai = {
                "role": "user",
                "content": [
                    {"type": "text", "text": user_input},
                    {"type": "image_url", "image_url": {"url": image_data}}  # This is kept only in memory
                ]
            }

            # Store a safe version (text only + display) in history
            session["history"].append({
                "role": "user",
                "content": user_input  # Only text stored in session
            })

            display_html = f'<img src="{image_data}" class="chat-image">'
            
        else:
            user_message_to_openai = {
                "role": "user",
                "content": user_input
            }
            session["history"].append(user_message_to_openai)

        # Create a temporary copy of full history (with real image content only in memory)
        history_for_openai = session["history"][:-1] + [user_message_to_openai]

        try:
            completion = openai.chat.completions.create(
                model="gpt-4o",
                messages=history_for_openai  # Use this instead of session["history"]
            )
            response = completion.choices[0].message.content.strip()
            session["history"].append({"role": "assistant", "content": response})
        except Exception as e:
            response = f"Error: {e}"
            session["history"].append({"role": "assistant", "content": response})

    return render_template(
        "index.html",
        response=response,
        user_input=user_input,
        history=session["history"],
        show_welcome=session.get("show_welcome", False),
        display_image=display_html
    )

@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)

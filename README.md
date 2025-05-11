# AI Chatbot Project 🤖

This is a simple AI-powered chatbot built using **Flask** for the final project in CS 4540 (AI Learning). The goal is to create a working chatbot web app that uses AI or language model prompts to provide useful responses.

## 💡 Project Goal
We're building a chatbot that:
- Answering user questions conversationally
- Recommending movies, games, and books (via preset buttons)
- Offering friendly advice (via preset button)
- Maintaining chat history per session
- Providing a responsive UI experience with loading animations and auto-scroll

This project is designed to be completed within a few weeks, focusing on getting a functional and presentable prototype.

---

## 🛠️ Tech Stack

| Layer        | Technology                  |
|--------------|-----------------------------|
| Backend      | Python (Flask)              |
| Frontend     | HTML, CSS, JS               |
| AI Engine    | OpenAI GPT-4o (via API)     |
| Environment  | Python-dotenv for API key   |
| UX Interacts | JavaScript (animation)      |
| Image Uploads| Base64 image encoding + PIL |
| Sessions     | Flask-Session (server-side) |
| Data Storage | SQLite (SQLAlchemy ORM)     |
| Env Config   | Python-dotenv               |



## 📁 Folder Structure
ai-chatbot/
├── static/
│   ├── style.css
│   ├── script.js
│   └── img/
│       └── background.jpg
├── templates/
│   ├── index.html
│   └── history.html
├── instance/
│   └── chat_history.db  ← (SQLite DB auto-generated)
├── app.py
├── .env
├── README.md
└── .gitignore


## ✅ Features
🧠 Conversational AI via GPT-4o

🖼️ Image upload and processing support

💬 Preset buttons for quick suggestions (Game, Movie, Book, Advice)

⏳ Typing indicator (three-dot animation)

🔁 Scrollable chat window with auto-scroll

🧽 “Clear Chat” button to reset session

💾 “View Saved History” with time-stamped logs

🎛️ Tab bar for Chat, Settings, Help

🎨 Elegant blurred-glass UI with full responsiveness

🔊 Text-to-Speech support for assistant replies

🧠 Session history stored using SQLite + SQLAlchemy
---

## 🚀 How to Run

1. Clone this repo:
git clone https://github.com/hoangle66/ai-chatbot.git
cd ai-chatbot

2. Install dependencies Flask: 

`pip install flask flask-session python-dotenv openai sqlalchemy gtts SpeechRecognition pillow beautifulsoup4`

3. Create a .env file with your API key:

`OPENAI_API_KEY=your-openai-key-here`

4. (Optional) Create a directory for session storage (run on terminal):
`mkdir flask_session`

5. Run the app: `python app.py`

6. Open your browser and go to `http://localhost:5000`

## 👨‍💻 Team Members
- Hoang Le (Dempsey) - Project setup, backend logic, OpenAI & image upload, JS enhancements
- Carlos Romero  – Navigation bar tab UI , Speech to Text, Frontend improvments
- Garen Astrounian - Chat history, Database Setup, Front End improvments
- Derek Shin
- Fabricio Reyes


## 📅 Timeline
- Week 1: Project setup, base Flask app
- Week 2: Chatbot logic, OpenAI API integration
- Week 3: UI polish, image upload, session handling
- Week 4: Chat history, tab bar, final refinements

---
## ✅ Features Completed

 - [x] GPT-4o text responses

 - [x] Upload images for visual discussion

 - [x] Preset buttons: 🎮 Game, 🎬 Movie, 📚 Book, 🧘 Advice

 - [x] Typing animation and polished chat flow

 - [x] Auto-scroll and scrollable window

 - [x] Stylish blurred-glass UI with background

- [x] Clear Chat + View Saved History buttons

- [x] Full chat log with timestamps

- [x] Server-side session persistence

- [x] SQLite + SQLAlchemy integration

- [x] Server-side session via Flask-Session

- [x] Tab navigation bar: Chat / Settings / Help

- [x] Responsive mobile-friendly layout
---

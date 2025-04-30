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
| Frontend     | HTML, CSS                   |
| AI Engine    | OpenAI GPT-4o (via API)     |
| Environment  | Python-dotenv for API key   |
| UX Interacts | JavaScript                  |
| Uploads      | Base64 image encoding + PIL |
| Sessions     | Flask-Session (server-side) |



## 📁 Folder Structure
ai-chatbot/ 
├── static/ 
│    └── style.css
│    └── img/ 
├── templates/
│    └── index.html 
├── app.py 
├── README.md 
├── .env (local)


## ✅ Features
- Conversational memory with session persistence
- Upload and send **images** to the bot (e.g. latte art, cards)
- Preset suggestion buttons (🎮 Game, 🎬 Movie, 📚 Book, 🧘 Advice)
- Typing animation (three dots) for a natural delay
- Scrollable, auto-scrolling chat window
- Stylish UI with mobile responsiveness
- Auto-focus input field
- Clear Chat to reset session
- AI supports image + text input in the same message

---

## 🚀 How to Run

1. Clone this repo:
git clone https://github.com/hoangle66/ai-chatbot.git
cd ai-chatbot

2. Install dependencies Flask: 
`pip install flask`, 

`pip install flask python-dotenv openai`

`pip install flask flask-session`

3. Create a .env file with your API key:

`OPENAI_API_KEY=your-openai-key-here`

4. (Optional) Create a directory for session storage (run on terminal):
`mkdir flask_session`

5. Run the app: `python app.py`

6. Open your browser and go to `http://localhost:5000`

## 👨‍💻 Team Members
- Dempsey (Hoang Le) (project setup & backend)
- Carlos Romero
- Garen Astrounian
- Derek Shin
- Fabricio Reyes


## 📅 Timeline
- Week 1: Setup + initial chatbot prototype
- Week 2–3: Add AI logic + polish UI
- Week 4: Final testing + video presentation

---
## ✅ Features Completed

 - [x] Continuous conversation using OpenAI Chat Completions

 - [x] Preset buttons for Game, Movie, Book recommendations

 - [x] Give Advice preset button

 - [x] Typing animation (3-dots) while bot is "thinking"

 - [x] Smooth, center-aligned typing indicator with compact box

 - [x] Scrollable chat window with auto-scroll to bottom

- [x] Stylish and mobile-friendly layout

- [x] Auto-focus input for faster chatting

- [x] Clear Chat button to reset session

- [x] Improved bot text formatting (line breaks for easier reading)

- [x] Server-side session via Flask-Session

- [x] Image upload support (base64 encoding)
---

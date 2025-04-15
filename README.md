# AI Chatbot Project 🤖

This is a simple AI-powered chatbot built using **Flask** for the final project in CS 4540 (AI Learning). The goal is to create a working chatbot web app that uses AI or language model prompts to provide useful responses.

## 💡 Project Goal
We're building a chatbot that:
- Answering user questions conversationally
- Recommending movies and games (via preset buttons)
- Maintaining chat history per session
- Providing a responsive UI experience with loading animations and auto-scroll

This project is designed to be completed within a few weeks, focusing on getting a functional and presentable prototype.

---

## 🛠️ Tech Stack

| Layer        | Technology                  |
|--------------|-----------------------------|
| Backend      | Python (Flask)              |
| Frontend     | HTML, CSS                   |
| AI Engine    | OpenAI GPT-3.5 Turbo        |
| Environment  | Python-dotenv for API key   |
| UX Interacts | JavaScript                  |



## 📁 Folder Structure
ai-chatbot/ 
# CSS and frontend assets
├── static/ 
    └── style.css
    # Background image
├── img/ 
# HTML templates 
├── templates/
    └── index.html 
# Flask backend 
├── app.py 
# Project overview
├── README.md 


## ✅ Features
- Simple frontend UI for interacting with the bot
- Flask backend to handle chat logic
- Clear structure to add more AI features later


## 🚀 How to Run
1. Clone this repo:
git clone https://github.com/hoangle66/ai-chatbot.git
cd ai-chatbot
2. Install dependencies Flask: `pip install flask`, `pip install flask python-dotenv openai`
3. Make sure to create a .env file locally within the ai-chatbot folder with the line: `OPENAI_API_KEY=your-openai-key-here`
4. Run the app: `python app.py`
5. Open your browser and go to `http://localhost:5000`

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
- [x] Preset buttons for **game/movie recommendations**
- [x] Typing animation while bot is "thinking"
- [x] Scrollable chat window that keeps latest messages in view
- [x] Stylish and mobile-friendly layout
- [x] Auto-focus input for fast chatting
- [x] Easy **Clear Chat** reset button
- [x] Dark-on-light contrast for better readability

---





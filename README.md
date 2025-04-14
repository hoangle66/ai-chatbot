# AI Chatbot Project 🤖

This is a simple AI-powered chatbot built using **Flask** for the final project in CS 4540 (AI Learning). The goal is to create a working chatbot web app that uses AI or language model prompts to provide useful responses.

## 💡 Project Goal
We're building a chatbot that:
- Answers casual and informative questions
- Remembers chat history within a session
- Feels responsive and user-friendly
- Can be extended with more AI features (e.g., game/movie recommendation logic)

This project is designed to be completed within a few weeks, focusing on getting a functional and presentable prototype.

---

## 🛠️ Tech Stack

| Layer        | Technology                  |
|--------------|-----------------------------|
| Backend      | Python (Flask)              |
| Frontend     | HTML, CSS                   |
| AI Engine    | OpenAI GPT-3.5 Turbo        |
| Environment  | Python-dotenv for API key   |

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
3. Run the app: `python app.py`
4. Open your browser and go to `http://localhost:5000`

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

- [x] OpenAI GPT API integration
- [x] Session-based memory for interactive chat
- [x] Stylized front-end using CSS and blur effect
- [x] Scrollable conversation area
- [x] Welcome message on first load
- [x] "Clear Chat" button to reset session
- [x] Environmental variable `.env` support for API key

---





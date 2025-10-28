# 🚀 Real-Time Chat Application with Flask & Socket.IO

## 📖 Description

This project is a **real-time web chat application** built using:

- **Python Flask**: Backend web framework  
- **Flask-SocketIO**: Enables real-time bi-directional communication between clients and server  
- **HTML / CSS / JS**: Frontend interface with a chat window, username input, message input, and dark/light mode toggle  

---

## ✨ Features

- Users can join the chat with a name or anonymously  
- Messages are displayed in **real-time** to all connected users  
- Each user’s messages appear on the **right**, others’ on the **left**  
- Messages are **color-coded** per user  
- Supports **image URLs**; if a message contains an image URL (ending with `.jpg`, `.png`, `.gif`), it is displayed as an image  
- **Dark/Light mode toggle** for better UX  

---

## 💻 How to Implement on Your System

### Prerequisites

- **Python 3.x** installed (`python --version` or `python3 --version`)  
- **pip** (Python package installer)  
- **Git** (optional, if you want to clone from GitHub)  

### Step 1: Clone or Download the Project

**With Git:**

```bash
git clone https://github.com/SATHIYAMURTHY-GIT/chat-application.git
cd chat-application
Or manually download the project ZIP from GitHub and extract it.

Step 2: Create a Virtual Environment (Optional but Recommended)
python -m venv venv


Activate it:

Windows:

venv\Scripts\activate


Mac/Linux:

source venv/bin/activate

Step 3: Install Required Packages
pip install flask flask-socketio eventlet


flask → backend web framework

flask-socketio → real-time messaging

eventlet → asynchronous server

Step 4: Run the Application
python app.py


The app will run on:
http://127.0.0.1:5000/ or http://localhost:5000/

Open the URL in a browser.

Step 5: Start Chatting

Enter your name (or leave empty for anonymous)

Type your message

If you enter an image URL, it will be displayed as an image in the chat

Open the same URL in multiple browser tabs to see real-time messages between users

Step 6: Optional – Push Changes to GitHub

After making changes:

git add .
git commit -m "Initial commit"
git push -u origin main

📝 Notes

Works on any modern browser (Chrome, Firefox, Edge)

Messages are color-coded and aligned for better readability

Dark/light mode is toggled via the switch on the top-right corner

Image URLs must be direct links ending with .jpg, .png, or .gif

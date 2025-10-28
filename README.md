# Chat Application

A simple real-time chat application built with Flask and Flask-SocketIO. Messages are exchanged in real time between clients and the server. Image URLs ending with .jpg, .png or .gif are displayed inline.

## Features
- Real-time messaging (Flask + Flask-SocketIO)
- Image URL preview for direct image links
- Dark / Light mode toggle
- Messages color-coded and aligned for readability
- Works in modern browsers (Chrome, Firefox, Edge)

---

## Prerequisites
- Python 3.8+
- Git (optional, for cloning the repo)

---

## Installation & Run (recommended)

1. Clone the repository (or download and extract the ZIP):
```bash
git clone https://github.com/SATHIYAMURTHY-GIT/chat-application.git
cd chat-application
```

2. (Optional but recommended) Create and activate a virtual environment:

Windows (PowerShell):
```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

Windows (cmd.exe):
```cmd
python -m venv venv
venv\Scripts\activate
```

macOS / Linux:
```bash
python -m venv venv
source venv/bin/activate
```

3. Install required packages:
```bash
pip install flask flask-socketio eventlet
```

(Alternatively you can create a `requirements.txt` with:
```
flask
flask-socketio
eventlet
```
and run `pip install -r requirements.txt`.)

4. Run the application:
```bash
python app.py
```

By default the app will be available at:
- http://127.0.0.1:5000/
- or http://localhost:5000/

Open the URL in multiple browser tabs to test real-time messaging.

---

## Usage
- Enter your name (leave empty to use "Anonymous")
- Type a message and send
- If you enter a direct image URL ending with `.jpg`, `.jpeg`, `.png`, or `.gif`, it will be displayed as an image in the chat
- Toggle dark/light mode using the switch at the top-right

---

## Notes & Tips
- Image URLs must be direct links to an image resource and typically end with `.jpg`, `.jpeg`, `.png`, or `.gif`.
- If you see issues with concurrent connections, ensure you're running with `eventlet` (it is installed and used by Flask-SocketIO in this project).
- If you make changes, you can push them back to GitHub:
```bash
git add .
git commit -m "Describe your change"
git push -u origin main
```

---

## Troubleshooting
- "Socket connection failed": check browser console and server logs; confirm server is running on the expected host/port.
- "Image not displayed": verify the URL is a direct image link (ends with `.jpg`, `.jpeg`, `.png`, or `.gif`) and is accessible from your browser.

---

If you'd like, I can:
- Add a `requirements.txt`
- Create a short CONTRIBUTING guide
- Add a simple systemd or Procfile example for deployment

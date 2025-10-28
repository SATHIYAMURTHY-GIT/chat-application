from flask import Flask, render_template
from flask_socketio import SocketIO, send
import eventlet  # Ensure eventlet is installed

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
# Explicitly set async_mode to eventlet for better compatibility
socketio = SocketIO(app, async_mode='eventlet')

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(data):
    """
    Handle incoming messages.
    data should be a dictionary with keys:
    - 'user': sender's name
    - 'msg': message content (text or image URL)
    """
    if isinstance(data, dict):
        user = data.get('user', 'Anonymous').strip() or 'Anonymous'
        message_text = data.get('msg', '').strip()
        if message_text:
            # Broadcast structured dictionary to all clients
            send({'user': user, 'msg': message_text}, broadcast=True)
            print(f"{user}: {message_text}")
    else:
        # fallback for plain strings
        text = str(data).strip()
        if text:
            send({'user': 'Anonymous', 'msg': text}, broadcast=True)
            print(f"Anonymous: {text}")

if __name__ == '__main__':
    # Use eventlet for async server
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)

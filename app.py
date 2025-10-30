from flask import Flask, render_template
from flask_socketio import SocketIO, send
import eventlet

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

# Enable CORS and force eventlet async mode
socketio = SocketIO(app, async_mode='eventlet', cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(data):
    """Handle incoming chat messages."""
    if isinstance(data, dict):
        user = data.get('user', 'Anonymous').strip() or 'Anonymous'
        message_text = data.get('msg', '').strip()
        if message_text:
            send({'user': user, 'msg': message_text}, broadcast=True)
            print(f"{user}: {message_text}")
    else:
        text = str(data).strip()
        if text:
            send({'user': 'Anonymous', 'msg': text}, broadcast=True)
            print(f"Anonymous: {text}")

if __name__ == '__main__':
    print("🚀 Chat app is running at http://127.0.0.1:5000")
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)

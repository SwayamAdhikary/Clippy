from flask import Flask, render_template, request, redirect, url_for, session
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Required for session management
socketio = SocketIO(app)

# Dictionary to store clipboard text for each topic
clipboard_data = {}

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/join', methods=['POST'])
def join():
    topic = request.form['topic']
    session['topic'] = topic  # Save topic in session
    return redirect(url_for('index'))

@app.route('/clipboard')
def index():
    if 'topic' not in session:
        return redirect(url_for('login'))  # Redirect if no topic is provided
    topic = session['topic']
    return render_template('index.html', topic=topic)

@socketio.on('text update')
def handle_text_update(data):
    topic = data['topic']
    text = data['text']
    clipboard_data[topic] = text  # Save the clipboard content for the specific topic
    emit('update text', {'text': text, 'topic': topic}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)

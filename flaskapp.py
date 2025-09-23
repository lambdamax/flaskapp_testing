from flask import Flask, request, render_template_string, session, jsonify
import os
import signal

app = Flask(__name__)
app.secret_key = 'super_secret_key'

# Simulate a simple in-memory 'database' to store user input
fake_db = {"user_input": ""}

@app.route('/store', methods=['POST'])
def store():
    user_input = request.form['input']
    fake_db['user_input'] = user_input  # Store the input in the 'database'
    return "Input stored successfully!"

@app.route('/get-stored-input')
def get_stored_input():
    # Return the stored input back to the user
    stored_input = fake_db['user_input']
    return render_template_string(f"<div>{stored_input}</div>")

@app.route('/')
def home():
    return '''
    <h1>Flask App Testing</h1>
    <h2>Store Input</h2>
    <form action="/store" method="POST">
        <label for="input">Enter some input:</label><br>
        <input type="text" name="input" id="input" required><br><br>
        <input type="submit" value="Store Input">
    </form>
    <br>
    <h2>Get Stored Input</h2>
    <a href="/get-stored-input">View Stored Input</a>
    '''

@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return jsonify(message='Shutting down...'), 200

def shutdown_server():
    os.kill(os.getpid(), signal.SIGINT)

if __name__ == '__main__':
    app.run(debug=True)


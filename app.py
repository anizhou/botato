from flask import Flask
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)  # Start ngrok when app is run

@app.route("/")
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run()
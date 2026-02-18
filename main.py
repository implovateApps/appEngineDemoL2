from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to App Engine – Serverless PaaS!"

@app.route("/about")
def about():
    return "This app is running without managing any VM."

if __name__ == "__main__":
    # Added standard port binding for local testing
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! Python Web App Successfully Deployed on Microsoft Azure"

if __name__ == "__main__":
    app.run()
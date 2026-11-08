from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to AWS-InfraWatch-Lite!</h1><p>Our Flask application is running successfully.</p>"

if __name__ == "__main__":
    app.run(debug=True)
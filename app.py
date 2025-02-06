# app.py
from flask import Flask

app = Flask(__name__)

@app.route("/api/v1/status")
def home():
    return "info: Everything looks good"

if __name__ == "__main__":
    app.run(debug=True)


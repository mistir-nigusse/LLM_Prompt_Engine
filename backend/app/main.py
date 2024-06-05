from app import app
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This should allow all domains by default. Adjust as needed.

if __name__ == "__main__":
    app.run(debug=True)

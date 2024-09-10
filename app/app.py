from dotenv import load_dotenv
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import User, MathHistory
from resources.user import user_bp
from resources.history import history_bp

app.register_blueprint(user_bp)
app.register_blueprint(history_bp)
@app.route("/", methods=["GET"])
def hello():
    return "Hello, World!"



if __name__ == "__main__":
    app.run(debug=True);
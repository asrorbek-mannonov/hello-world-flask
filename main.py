from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

with app.app_context():
    db.create_all()

@app.route("/")
def hello_world():
    try:
        db.session.execute(text('SELECT 1'))
        return jsonify({"message": "Hello, World!", "db_connection": "OK"})
    except Exception as e:
        return jsonify({"message": "Hello, World!", "error": str(e), "db_connection": "NOT OK"})
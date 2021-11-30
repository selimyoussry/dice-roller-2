import random

from flask import Flask, jsonify, render_template


app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"roll": random.randint(1, 6)})

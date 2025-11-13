from flask import Flask, jsonify
import random

app = Flask(__name__)

MOTIVATIONAL_QUOTES = [
    "Automate what you hate.",
    "Ship small, ship often.",
    "Tests are your future self's best friend.",
    (
        "If it hurts, do it more often "
        "— then automate it."
    ),
    "Good DevOps is invisible; only failures are loud.",
]


@app.route("/")
def hello() -> str:
    """Return greeting for root endpoint."""
    return "Hello, DevOps World!"


@app.route("/motivator")
def motivator():
    """Return a random DevOps motivational quote as JSON."""
    quote = random.choice(MOTIVATIONAL_QUOTES)
    return jsonify({"quote": quote})


if __name__ == "__main__":
    app.run()

from flask import Flask, jsonify, request
from flask_cors import CORS
import random
import os

app = Flask(__name__)
CORS(app)  # so Next.js can talk to us

HAMSTER_QUOTES = [
    "Running… running… running… almost there!",
    "Please insert more sunflower seeds for faster performance.",
    "Your request is now in our hamster wheel queue.",
    "Squeak! Data retrieved successfully."
]

@app.route("/healthz")
def healthz():
    return jsonify({"status": "ok", "message": "HamsterCloud is spinning happily!"})

@app.route("/compute")
def compute():
    task = request.args.get("task", "spin wheel")
    return jsonify({
        "task": task,
        "result": f"Hamsters completed: {task} ✅",
        "quote": random.choice(HAMSTER_QUOTES)
    })

@app.route("/echo", methods=["POST"])
def echo():
    data = request.get_json() or {}
    return jsonify({"you_said": data, "note": "Hamsters heard you loud and clear!"})

if __name__ == "__main__":
    port = int(os.getenv("PORT", "8000"))
    app.run(host="0.0.0.0", port=port)

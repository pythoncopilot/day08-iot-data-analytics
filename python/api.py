from flask import Flask, jsonify, request
from flask_cors import CORS
from db import init_db, log_control
import sqlite3

app = Flask(__name__)
CORS(app)

init_db()

device_state = {
    "light": 0,
    "fan": 0,
    "ac": 24,
    "kitchen": 0,
    "bath": 0,
    "tv": 0,
    "garage": 0
}


@app.route("/latest")
def latest():
    return jsonify(device_state)


@app.route("/control", methods=["POST"])
def control():
    global device_state
    data = request.json

    for key in device_state:
        if key in data:
            device_state[key] = data[key]
            log_control(key, data[key])

    return jsonify({"status": "ok", "state": device_state})


@app.route("/history")
def history():
    conn = sqlite3.connect("database/iot_data.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT device, value, timestamp
        FROM control_history
        ORDER BY id DESC
        LIMIT 20
    """)

    rows = cursor.fetchall()
    conn.close()

    return jsonify([
        {"device": r[0], "value": r[1], "timestamp": r[2]}
        for r in rows
    ])


if __name__ == "__main__":
    app.run(debug=True, port=5000)
import sqlite3
from datetime import datetime

DB = "database/iot_data.db"


def init_db():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS control_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            device TEXT,
            value INTEGER,
            timestamp TEXT
        )
    """)

    conn.commit()
    conn.close()


def log_control(device, value):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO control_history (device, value, timestamp)
        VALUES (?, ?, ?)
    """, (
        device,
        value,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()
    conn.close()
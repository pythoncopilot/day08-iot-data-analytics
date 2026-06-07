import sqlite3

DB = "database/iot_data.db"


def analyze():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT device, value, timestamp
        FROM control_history
    """)

    data = cursor.fetchall()
    conn.close()

    if not data:
        print("No data found")
        return

    print("\n📊 IoT ANALYTICS REPORT")
    print("-" * 40)

    #print("Total Actions:", len(data))
    print("TOTAL ACTION COUNT:", len(data))
    device_count = {}

    for device, value, ts in data:
        device_count[device] = device_count.get(device, 0) + 1

    print("\nMost Active Devices:")
    for k, v in sorted(device_count.items(), key=lambda x: x[1], reverse=True):
        print(f"{k}: {v}")

    print("\nLast 5 Events:")
    for row in data[-5:]:
        print(row)


if __name__ == "__main__":
    analyze()
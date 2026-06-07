import json
import random
import time
import urllib.error
import urllib.request

API = "http://127.0.0.1:5000/control"

print("Running SIMULATION MODE...\n")

while True:
    payload = {
        "light": random.randint(0, 1),
        "fan": random.randint(0, 100),
        "ac": random.randint(18, 30)
    }

    print("Sending:", payload)

    try:
        data = json.dumps(payload).encode("utf-8")
        request = urllib.request.Request(
            API,
            data=data,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with urllib.request.urlopen(request, timeout=5) as response:
            response.read()
    except urllib.error.URLError:
        print("API not running")

    time.sleep(2)
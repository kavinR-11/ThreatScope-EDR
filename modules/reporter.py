import json
from datetime import datetime


def write_incident(alerts):

    if not alerts:
        return

    timestamp = datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")

    filename = f"reports\\incident_{timestamp}.json"

    report = {
        "timestamp": timestamp,
        "alerts": alerts
    }

    with open(filename, "w") as f:
        json.dump(report, f, indent=4)

    print("[+] Incident report created:", filename)

import psutil
import json


def load_config():
    with open("config.json", "r") as f:
        return json.load(f)


def scan_processes():

    config = load_config()
    alerts = []

    for proc in psutil.process_iter(['pid', 'name', 'exe', 'cpu_percent']):
        try:

            cpu = proc.info['cpu_percent']
            exe = proc.info['exe'] or ""

            if cpu > config["cpu_threshold"]:
                alerts.append({
                    "type": "HIGH_CPU",
                    "process": proc.info['name'],
                    "pid": proc.info['pid'],
                    "cpu": cpu,
                    "path": exe
                })

            for path in config["suspicious_paths"]:
                if exe.startswith(path):
                    alerts.append({
                        "type": "SUSPICIOUS_LOCATION",
                        "process": proc.info['name'],
                        "pid": proc.info['pid'],
                        "path": exe
                    })

        except:
            pass

    return alerts

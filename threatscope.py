import time
from modules.process_monitor import scan_processes
from modules.reporter import write_incident


print("ThreatScope v1 started")
print("Monitoring system activity...\n")


while True:

    alerts = scan_processes()

    if alerts:

        for alert in alerts:
            print("[ALERT]", alert)

        write_incident(alerts)

    time.sleep(5)

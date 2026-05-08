#!/usr/bin/env python3
import subprocess
import time
import os
import json
import numpy as np
from datetime import datetime
from sklearn.ensemble import IsolationForest

# --- CONFIGURATION ---
LOG_FILE = [log dir]
AI_LOG_FILE = [wazuh log dir]
WINDOW_SIZE = 20
CHECK_INTERVAL = 10

print(f"[*] AI Hybrid Engine Started. Logging to: {AI_LOG_FILE}")

clf = IsolationForest(n_estimators=100, contamination=0.01, random_state=42)
traffic_history = []

def get_file_pos():
    return os.stat(LOG_FILE).st_size

def count_new_logs(start_pos):
    try:
        current_pos = get_file_pos()
        if current_pos < start_pos: return 0, current_pos
        with open(LOG_FILE, 'r') as f:
            f.seek(start_pos)
            new_lines = len(f.readlines())
        return new_lines, current_pos
    except:
        return 0, start_pos

def inject_syslog(message):
    """Inject RFC 3164 formatted log directly into syslog for Wazuh pickup."""
    timestamp = datetime.now().strftime("%b %e %H:%M:%S")
    log_line = f"{timestamp} sentinel-core OpenSec-AI[{os.getpid()}]: {message}\n"
    subprocess.run(
        ["sudo", "tee", "-a", "/var/log/syslog"],
        input=log_line,
        text=True,
        capture_output=True
    )

current_pos = get_file_pos()

while True:
    time.sleep(CHECK_INTERVAL)

    # 1. Get Data
    new_count, current_pos = count_new_logs(current_pos)
    traffic_history.append(new_count)
    if len(traffic_history) > WINDOW_SIZE:
        traffic_history.pop(0)

    if len(traffic_history) == WINDOW_SIZE:
        data = np.array(traffic_history).reshape(-1, 1)

        # === STATISTICAL ===
        mean = np.mean(traffic_history)
        std = np.std(traffic_history)
        stat_threshold = mean + (3 * std)
        if stat_threshold < 5: stat_threshold = 5
        stat_status = "ANOMALY" if new_count > stat_threshold else "NORMAL"

        # === ML (ISOLATION FOREST) ===
        clf.fit(data)
        pred = clf.predict([[new_count]])[0]
        ml_status = "ANOMALY" if (pred == -1 and new_count > mean) else "NORMAL"

        # === HYBRID DECISION ===
        final_decision = "BLOCK" if (stat_status == "ANOMALY" and ml_status == "ANOMALY") else "MONITOR"

        # === GENERATE JSON LOG (Local Backup) ===
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "app": "OpenSec-AI",
            "traffic_count": new_count,
            "statistical_model": {
                "status": stat_status,
                "threshold": round(stat_threshold, 2)
            },
            "ml_model": {
                "status": ml_status,
                "algorithm": "IsolationForest"
            },
            "final_action": final_decision
        }
        with open(AI_LOG_FILE, 'a') as f:
            f.write(json.dumps(log_entry) + "\n")

        # === WAZUH SYSLOG INJECTION ===
        if final_decision == "BLOCK":
            inject_syslog("BLOCK - Anomaly intercepted")
        else:
            inject_syslog("MONITOR - Routine heartbeat")

        print(f"Logged: {final_decision} (Traffic: {new_count})")

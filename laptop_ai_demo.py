import time
import numpy as np
import psutil
from sklearn.ensemble import IsolationForest
from datetime import datetime

print("[*] Starting Edge AI Monitor (Laptop Sandboxed PoC)")
print("[*] Learning baseline network traffic... (Browse the web normally for 20 seconds)")

history = []
# We use contamination=0.1 assuming 10% of traffic spikes might be anomalies
clf = IsolationForest(contamination=0.1, random_state=42)

while True:
    # 1. Measure network traffic over 1 second
    net1 = psutil.net_io_counters().bytes_recv
    time.sleep(1)
    net2 = psutil.net_io_counters().bytes_recv
    
    # 2. Convert to Kilobytes per second (KB/s)
    kbps = (net2 - net1) / 1024.0
    
    # 3. Add to history buffer
    history.append(kbps)
    if len(history) > 30: # Keep memory footprint tiny (Edge AI simulation)
        history.pop(0)
        
    # 4. Run the AI once we have enough baseline data
    if len(history) >= 15:
        data = np.array(history).reshape(-1, 1)
        
        # --- ML MODEL (Isolation Forest) ---
        clf.fit(data)
        pred = clf.predict([[kbps]])[0]
        ml_status = "🚨 ANOMALY" if (pred == -1 and kbps > np.mean(history)) else "✅ NORMAL"
        
        # --- STATISTICAL MODEL (Z-Score) ---
        mean = np.mean(history)
        std = np.std(history)
        threshold = mean + (3 * std)
        if threshold < 50: threshold = 50 # Minimum noise floor
        stat_status = "🚨 ANOMALY" if kbps > threshold else "✅ NORMAL"
        
        # Output the live comparison
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Traffic: {kbps:8.2f} KB/s | Stat: {stat_status:12} | ML (iForest): {ml_status}")
    else:
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Traffic: {kbps:8.2f} KB/s | Calibrating... ({len(history)}/15)")

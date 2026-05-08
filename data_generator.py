import pandas as pd
import numpy as np
import random

# CONFIG
HOURS = 24
SAMPLES_PER_HOUR = 60 # One check every minute
TOTAL_SAMPLES = HOURS * SAMPLES_PER_HOUR

print(f"[*] Generating {TOTAL_SAMPLES} minutes of 'Real-Life' traffic data...")

# 1. Generate "Normal" Background Traffic (Poisson Distribution)
# Real networks are never flat; they are "bursty" but low volume.
timestamps = pd.date_range(start="2026-02-01", periods=TOTAL_SAMPLES, freq="min")
traffic = np.random.poisson(lam=15, size=TOTAL_SAMPLES) # Avg 15 logs/min

# 2. Add "Daily Cycle" (More traffic at noon, less at night)
# This adds a sine wave to simulate human behavior
hour_modifier = 10 * np.sin(np.linspace(0, 3.14, TOTAL_SAMPLES))
traffic = traffic + hour_modifier
traffic = np.maximum(traffic, 0) # No negative logs

# 3. Inject Attacks
labels = np.zeros(TOTAL_SAMPLES) # 0 = Normal, 1 = Attack

# Attack A: The "Smash and Grab" (DDoS) - Easy for everyone to catch
# At hour 10 (Minute 600)
traffic[600:610] += 500 
labels[600:610] = 1

# Attack B: The "Stealth Infiltration" (Low & Slow) - The Faculty "Gotcha"
# At hour 18 (Minute 1080), attacker stays JUST below the radar
# A statistical model looking for "Mean + 3*SD" might miss this if SD is high
traffic[1080:1140] += 35 
labels[1080:1140] = 1

# 4. Save
df = pd.DataFrame({'timestamp': timestamps, 'volume': traffic, 'is_attack': labels})
df.to_csv('research_dataset.csv', index=False)
print("[+] Dataset saved to 'research_dataset.csv'")

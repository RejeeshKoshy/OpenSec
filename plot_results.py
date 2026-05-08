import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the results
print("[*] Loading final_results.csv...")
df = pd.read_csv('final_results.csv')

# 2. Setup the Plot (3 rows, 1 column)
plt.figure(figsize=(12, 10))

# --- PLOT 1: GROUND TRUTH (The Reality) ---
plt.subplot(3, 1, 1)
plt.plot(df.index, df['volume'], color='black', alpha=0.6, linewidth=1, label='Traffic Volume')
# Shade the area where "is_attack" is 1
plt.fill_between(df.index, 0, df['volume'].max(), where=df['is_attack']==1, 
                 color='gray', alpha=0.5, label='Actual Attack Phase')
plt.title('Ground Truth: Actual Network Traffic & Attacks', fontsize=12, fontweight='bold')
plt.ylabel('Log Volume')
plt.legend(loc='upper right')
plt.grid(True, alpha=0.3)

# --- PLOT 2: STATISTICAL MODEL (The "Dumb" One) ---
plt.subplot(3, 1, 2)
# Show faint background traffic for context
plt.plot(df.index, df['volume'], color='gray', alpha=0.2)
# Highlight detections in RED
plt.fill_between(df.index, 0, df['volume'].max(), where=df['pred_stat']==1, 
                 color='red', alpha=0.6, label='Statistical Detection')
plt.title('Model A: Statistical (Z-Score) - Missed the Stealth Attack', fontsize=12, fontweight='bold')
plt.ylabel('Detection')
plt.legend(loc='upper right')
plt.grid(True, alpha=0.3)

# --- PLOT 3: ML MODEL (The "Smart" One) ---
plt.subplot(3, 1, 3)
plt.plot(df.index, df['volume'], color='gray', alpha=0.2)
# Highlight detections in BLUE
plt.fill_between(df.index, 0, df['volume'].max(), where=df['pred_ml']==1, 
                 color='blue', alpha=0.6, label='ML Detection')
plt.title('Model B: Machine Learning (Isolation Forest) - Caught Both', fontsize=12, fontweight='bold')
plt.ylabel('Detection')
plt.xlabel('Time (Minutes)')
plt.legend(loc='upper right')
plt.grid(True, alpha=0.3)

# 3. Save it
plt.tight_layout()
plt.savefig('research_victory_graph.png', dpi=300)
print("[+] Graph saved to 'research_victory_graph.png'")

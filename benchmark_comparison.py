import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.metrics import precision_score, recall_score, f1_score

# 1. Load the Dataset you just made
print("[*] Loading research_dataset.csv...")
df = pd.read_csv('research_dataset.csv')
X = df[['volume']].values

# === MODEL A: STATISTICAL (Z-Score) ===
# Logic: Calculate Mean + 3*StdDev. Anything higher is an anomaly.
mean = df['volume'].mean()
std = df['volume'].std()
threshold = mean + (3 * std)
df['pred_stat'] = np.where(df['volume'] > threshold, 1, 0)

# === MODEL B: ML (Isolation Forest) ===
# Logic: Use the Isolation Forest algorithm to find anomalies.
# contamination=0.02 means we expect about 2% of data to be attacks.
clf = IsolationForest(contamination=0.02, random_state=42)
clf.fit(X)
# The model returns -1 for anomaly, 1 for normal. We convert this to 1 and 0.
df['pred_ml'] = np.where(clf.predict(X) == -1, 1, 0)

# === SCORING FUNCTION ===
def print_scores(name, y_true, y_pred):
    p = precision_score(y_true, y_pred, zero_division=0)
    r = recall_score(y_true, y_pred, zero_division=0)
    f1 = f1_score(y_true, y_pred, zero_division=0)
    
    print(f"\n--- {name} Results ---")
    print(f"Precision: {p:.2f} (Trustworthiness)")
    print(f"Recall:    {r:.2f} (Detection Rate)")
    print(f"F1-Score:  {f1:.2f} (Overall Balance)")

# Print the comparison
print_scores("Statistical (Z-Score)", df['is_attack'], df['pred_stat'])
print_scores("ML (Isolation Forest)", df['is_attack'], df['pred_ml'])

# Save detailed results for graphing later
df.to_csv('final_results.csv', index=False)
print("\n[+] Detailed results saved to 'final_results.csv'")

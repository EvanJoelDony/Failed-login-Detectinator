import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("login_data.csv")

# --- Your analysis code here (counts, suspicious IPs, etc.) ---

# --- Visualization ---
sns.countplot(x="status", data=df)
plt.title("Login Attempts: Success vs Failure")
plt.show()

df["timestamp"] = pd.to_datetime(df["timestamp"])
df.set_index("timestamp").resample("D").size().plot()
plt.title("Login Attempts Over Time")
plt.ylabel("Attempts")
plt.show()


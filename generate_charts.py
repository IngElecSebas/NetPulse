import os
import sqlite3
import matplotlib.pyplot as plt
from collections import defaultdict

# Ensure the charts/ folder exists
CHARTS_DIR = "charts"
os.makedirs(CHARTS_DIR, exist_ok=True)

# SQLite Database Configuration
DB_NAME = "netpulse_metrics.db"

def extract_data():
    """Extract latency data from the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("SELECT timestamp, target, latency_ms FROM metrics ORDER BY timestamp")
    rows = cursor.fetchall()
    conn.close()

    # Organize data by target
    data = defaultdict(list)
    for timestamp, target, latency in rows:
        data[target].append((timestamp, latency))

    return data

def generate_chart(data):
    """Generate and save the line chart."""
    plt.figure(figsize=(12, 6))

    for target, records in data.items():
        # Separate timestamps and latencies
        timestamps = [record[0] for record in records]
        latencies = [record[1] for record in records]

        plt.plot(timestamps, latencies, label=target)

    plt.title("Network Performance Over Time", fontsize=16)
    plt.xlabel("Timestamp", fontsize=12)
    plt.ylabel("Latency (ms)", fontsize=12)
    plt.legend(title="Targets", fontsize=10)
    plt.grid(True, linestyle='--', alpha=0.6)

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45, fontsize=8)

    # Save the chart to the charts/ folder
    output_path = os.path.join(CHARTS_DIR, "network_performance.png")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
    print(f"Chart saved at: {output_path}")

if __name__ == "__main__":
    print("Extracting data from the database...")
    data = extract_data()

    if not data:
        print("No data found in the database.")
    else:
        print("Generating chart...")
        generate_chart(data)
        print("Chart generation complete.")
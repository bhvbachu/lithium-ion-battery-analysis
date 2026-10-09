
import csv
import matplotlib.pyplot as plt

data = []

# Read data
with open("battery_data.csv", "r") as f:
    for r in csv.DictReader(f):
        try:
            data.append({
                "t": float(r["Time"]),
                "v": float(r["Voltage"]),
                "i": float(r["Current"]),
                "temp": float(r["Temperature"]),
                "c": int(r["Cycle"])
            })
        except:
            pass

if not data:
    print("No valid data found!")
else:
    # Calculate energy and capacity
    energy = 0
    capacity = 0

    for a, b in zip(data, data[1:]):
        dt = abs(b["t"] - a["t"]) / 3600
        energy += a["v"] * abs(a["i"]) * dt
        capacity += abs(a["i"]) * dt

    # Cycle-wise temperature
    cycles = sorted(set(x["c"] for x in data))
    temps = [
        sum(x["temp"] for x in data if x["c"] == c) /
        len([x for x in data if x["c"] == c])
        for c in cycles
    ]

    # Prepare graph data
    t = [x["t"] for x in data]
    v = [x["v"] for x in data]
    i = [x["i"] for x in data]
    avg_temp = sum(x["temp"] for x in data) / len(data)

    # Display output in Command Prompt
    print("\n--- BATTERY ANALYSIS ---")
    print("Records:", len(data))
    print("Cycles:", len(cycles))
    print("Energy:", round(energy, 2), "Wh")
    print("Capacity:", round(capacity, 2), "Ah")
    print("Average Temperature:", round(avg_temp, 2), "°C")

    # Display three graphs in one separate window
    fig, ax = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle("Lithium-Ion Battery Analysis", fontsize=16)

    ax[0].plot(t, v, marker="o")
    ax[0].set_title("Voltage vs Time")
    ax[0].set_xlabel("Time")
    ax[0].set_ylabel("Voltage (V)")
    ax[0].grid(True)

    ax[1].plot(t, i, marker="o")
    ax[1].set_title("Current vs Time")
    ax[1].set_xlabel("Time")
    ax[1].set_ylabel("Current (A)")
    ax[1].grid(True)

    ax[2].plot(cycles, temps, marker="o")
    ax[2].set_title("Temperature vs Cycle")
    ax[2].set_xlabel("Cycle")
    ax[2].set_ylabel("Temperature (°C)")
    ax[2].grid(True)

    plt.tight_layout()
    plt.show()

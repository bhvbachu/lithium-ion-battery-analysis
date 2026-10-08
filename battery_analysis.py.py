# Lithium-Ion Battery Charging and Discharging Analysis

voltage = float(input("Enter battery voltage (V): "))
current = float(input("Enter current (A): "))
time = float(input("Enter time (hours): "))
temperature = float(input("Enter temperature (°C): "))

# Calculations
power = voltage * current
energy = power * time
capacity = current * time

# Temperature analysis
if temperature > 45:
    temperature_status = "High"
else:
    temperature_status = "Normal"

# Battery performance analysis
if temperature <= 45 and voltage >= 3.0 and capacity > 0:
    performance = "Good"
else:
    performance = "Needs Attention"

# Output
print("\n--- Battery Analysis ---")
print("Voltage:", voltage, "V")
print("Current:", current, "A")
print("Temperature:", temperature, "°C")
print("Power:", power, "W")
print("Energy:", energy, "Wh")
print("Capacity:", capacity, "Ah")
print("Temperature Status:", temperature_status)
print("Battery Performance:", performance)
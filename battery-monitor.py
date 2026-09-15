# Example 6 — Battery Safety Monitor

print("=== Battery Safety Monitor ===")

voltage = float(input("Enter battery voltage: "))
temperature = float(input("Enter battery temperature in °C: "))

voltage_safe = 12.0 <= voltage <= 13.0
temperature_safe = temperature < 45.0

battery_safe = voltage_safe and temperature_safe

print()

if battery_safe:
    print(" Battery readings are within the example safe range.")
else:
    print(" Battery readings need attention.")

    if not voltage_safe:
        print("- Check battery voltage.")

    if not temperature_safe:
        print("- Check battery temperature.")

"""
Challenge

Add a third condition:

Battery physically damaged? yes/no
"""
# Example 3 — Is the Robot Ready?

print("=== Robot Readiness Check ===")

battery_ok = input("Is the battery connected and charged? (yes/no): ").lower() == "yes"
code_ok = input("Has the robot code been tested? (yes/no): ").lower() == "yes"
inspection_ok = input("Has the robot passed inspection? (yes/no): ").lower() == "yes"
radio_ok = input("Is the radio connected? (yes/no): ").lower() == "yes"
driver_station_ok = input("Is the driver station working? (yes/no): ").lower() == "yes"

robot_ready = battery_ok and code_ok and inspection_ok and radio_ok and driver_station_ok

print()

if robot_ready:
    print("Robot is ready for the match!")

else:
    print("Robot is NOT ready.")
    print("Check the missing requirements.")
    for i, (req, is_ok) in enumerate([
        ("Battery", battery_ok),
        ("Code", code_ok),
        ("Inspection", inspection_ok),
        ("Radio", radio_ok),
        ("Driver Station", driver_station_ok)
    ]):
        if not is_ok:
            print(f"The missing requirement is: {req}")

"""
Challenge

Add two more requirements:

Radio connected

Driver station working

Bonus: Print exactly which requirement failed instead of only saying the robot is not ready.
"""
# Example 7 — Command-Line Robot Calculator

import sys
# How would you run this file?

if len(sys.argv) != 3:
    print("Usage: python3 robot_calc.py <motor_count> <motors_per_side>")
    sys.exit(1)

motor_count = int(sys.argv[1])
motors_per_side = int(sys.argv[2])

total_motors = motor_count * motors_per_side

print(f"Motor groups: {motor_count}")
print(f"Motors per group: {motors_per_side}")
print(f"Total motors: {total_motors}")


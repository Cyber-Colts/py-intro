# Example 8 — Robot Status CLI with argparse

# python3 robot_status.py --team 10211 --battery 12.6 --ready

import argparse

parser = argparse.ArgumentParser(
    description="FRC Robot Status Tool"
)

parser.add_argument(
    "--team",
    type=int,
    required=True,
    help="Team number"
)

parser.add_argument(
    "--battery",
    type=float,
    required=True,
    help="Battery voltage"
)

parser.add_argument(
    "--ready",
    action="store_true",
    help="Mark the robot as ready"
)

args = parser.parse_args()

print("=== Robot Status ===")
print(f"Team: {args.team}")
print(f"Battery voltage: {args.battery:.2f} V")
print(f"Robot marked ready: {args.ready}")

if args.battery < 12.0:
    print(" Battery voltage is low.")

if args.ready and args.battery >= 12.0:
    print(" Robot status looks good.")
else:
    print(" Robot needs additional checks.")
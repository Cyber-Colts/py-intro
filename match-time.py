print("=== Match Time Calculator ===")

match_duration = int(input("How long is the match in seconds? "))
elapsed_time = int(input("How many seconds have passed? "))

remaining_time = match_duration - elapsed_time

if remaining_time > 0:
    print(f" Time remaining: {remaining_time} seconds")
elif remaining_time == 0:
    print(" Match is over!")
else:
    print(" The entered time is greater than the match duration.")

"""
Challenge

Add match phases:

0–15 seconds     → Autonomous
16–135 seconds   → Teleoperated
136+ seconds     → Endgame
"""
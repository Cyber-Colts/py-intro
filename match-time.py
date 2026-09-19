print("=== Match Time Calculator ===")

match_duration = int(135)
elapsed_time = int(input("How many seconds have passed? "))

remaining_time = match_duration - elapsed_time

if remaining_time > 0:
    print(f" Time remaining: {remaining_time} seconds")
elif remaining_time == 0:
    print(" Match is over!")
elif remaining_time >= 20:
    print(" Time for autonomous!")
elif remaining_time >= 21 and remaining_time <= 135:
    print(" Time for teleoperated!")
elif remaining_time >= 136:
    print(" Time for endgame!")
else:
    print(" The entered time is greater than the match duration.")

"""Challenge

Add match phases:

0–20 seconds     → Autonomous
21-135 seconds   → Teleoperated
136+ seconds     → Endgame
"""
print("=== Simple FRC Scouting Card ===")

team_number = int(input("Team number: "))
scout_name = input("Scout name: ")

auto_points = int(input("Autonomous points: "))
teleop_points = int(input("Teleoperated points: "))
endgame_points = int(input("Endgame points: "))

climbed = input("Did the robot complete its endgame task? (yes/no): ").lower() == "yes"

total_score = auto_points + teleop_points + endgame_points

print("\n=== Scouting Report ===")
print(f"Team: {team_number}")
print(f"Scout: {scout_name}")
print(f"Total points: {total_score}")
print(f"Completed endgame: {climbed}")

if total_score >= 50:
    print("Performance: High scoring match")
elif total_score >= 25:
    print("Performance: Moderate scoring match")
else:
    print("Performance: Low scoring match")


"""
Calculate:
Add:

Number of penalties

Number of successful scoring attempts

Number of failed scoring attempts
Accuracy = successful attempts / total attempts × 100
"""
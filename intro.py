# Example 1 — Team Introduction

print("=== FRC Team Introduction ===")

team_name = input("What is your team name? ") # define team name
team_number = input("What is your team number? ") # define team number 
student_name = input("What is your name? ") # define the students name

print() # print text brought from vars
print(f"Welcome, {student_name.capitalize()}!") 
print(f"You are part of {team_name.capitalize()}, Team #{team_number}.")
print("Let's build something awesome!")

""" 
Challenge:
Add proper capitalization to the team name and student name.
"""
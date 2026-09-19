# Example 2 — Robot Battery Calculator

print("=== Robot Battery Calculator ===")

total_batteries = int(input("How many batteries does the team have? "))
charged_batteries = int(input("How many are currently charged? "))

uncharged_batteries = total_batteries - charged_batteries
uncharged_batteries_p = charged_batteries/total_batteries*100

print()
print(f"Total batteries: {total_batteries}")
print(f"Charged batteries: {charged_batteries}")
print(f"Batteries still needing charge: {uncharged_batteries}")
print(f"Percentage of batteries still needing charge: {uncharged_batteries_p:.2f}%")

"""
Challenge

Add:

Number of batteries currently in use

Number of batteries available for the next match

Extra challenge: Calculate the percentage of batteries that are charged.
"""
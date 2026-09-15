print("=== Robot Battery Calculator ===")

total_batteries = int(input("How many batteries does the team have? "))
charged_batteries = int(input("How many are currently charged? "))

uncharged_batteries = total_batteries - charged_batteries

print()
print(f"Total batteries: {total_batteries}")
print(f"Charged batteries: {charged_batteries}")
print(f"Batteries still needing charge: {uncharged_batteries}")
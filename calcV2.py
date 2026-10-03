operation = input("What is the operation you want to perform? (+ for sum, - for subtraction also multiplication X and / for division): ")
number1 = int(input("What is your first value? "))
number2 = int(input("What is your second value? "))

print("The values are:", number1, "and", number2)

if operation == "+":
    number3 = number1 + number2
elif operation == "-":
    number3 = number1 - number2
elif operation == "X" or operation == "x":
    number3 = number1 * number2
elif operation == "/":
    number3 = number1 / number2

print("The result is:", number3)
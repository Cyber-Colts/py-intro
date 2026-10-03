# Make a simple calculator
"""
Input, operadores de numeros, manejo de errores, intefaz de usuario basica. 
"""
#USER INTERFACE
typeofmath = input("What mathematical operation would you like to solve?")

sum = input
substraction = input
sumresult = float(firstvalue) + float(secondvalue)
subresult = float(firstvalue) - float(secondvalue)


print ("What is your first value?")
firstvalue = int(input())
print("What is your second value?")
secondvalue = int(input())

print("The values are:", firstvalue, "and", secondvalue)

if typeofmath == sum:
    print("The result is:", sumresult)

if typeofmath == substraction:
    print("The result is:", subresult)

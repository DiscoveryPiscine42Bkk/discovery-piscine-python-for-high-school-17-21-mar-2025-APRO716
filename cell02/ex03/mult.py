#!/usr/bin/env python3

Num1 = int(input("Enter the first number: "))
Num2 = int(input("Enter the second number: "))
Result = Num1*Num2

print(str(Num1) + " x " + str(Num2) + " =" , Result)

if Result < 0:
    print("The result is negative.")
elif Result == 0:
    print("The result is both positve and negative.")
else:
    print("The result is positve.")
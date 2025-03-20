print("Give me the first number: ")
num1 = float(input())
print("Give me the second number: ")
num2 = float(input())
print("Thank You!")
try:
    print(f"{num1} + {num2} = {num1 + num2}")
    print(f"{num1} - {num2} = {num1 - num2}")
    print(f"{num1} / {num2} = {num1 / num2}") #y it shows decimal 0 bruh :sob:
    print(f"{num1} x {num2} = {num1 * num2}")

except ZeroDivisionError:
    print(f"{num1} / {num2} = Undefined") # / 0 is not allowed & fix ZeroDivisionError error
    print(f"{num1} x {num2} = {num1 * num2}") # add ts again to keep running till the end ts pmo :broken_heart:
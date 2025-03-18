import math

num_input = input("Give me a number: ")

try:
    num = float(num_input)
    rounded_up = math.ceil(num)
    print(rounded_up)
except ValueError:
    print("Invalid input. Please enter a number.")
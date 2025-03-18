num_input = input("Give me a number: ")

try:
    num = float(num_input)
    if num == int(num):
        print("This number is an integer.")
    else:
        print("This number is a decimal.")
except ValueError:
    print("Invalid input. Please enter a number.")
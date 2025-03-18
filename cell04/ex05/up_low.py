#!/usr/bin/env python3

user_input = input("Enter a string: ")

swapped_string = ""
for char in user_input:
    if char.islower():
        swapped_string += char.upper()
    elif char.isupper():
        swapped_string += char.lower()
    else:
        swapped_string += char  #wth

print(swapped_string)
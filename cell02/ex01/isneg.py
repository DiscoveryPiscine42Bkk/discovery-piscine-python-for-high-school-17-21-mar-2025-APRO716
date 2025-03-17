#!/usr/bin/env python3

Number = int(input("Enter a number: "))

if Number < 0:
    print("This number is negative.")
elif Number == 0:
    print("This number is both positve and negative.")
else:
    print("This number is positve.")
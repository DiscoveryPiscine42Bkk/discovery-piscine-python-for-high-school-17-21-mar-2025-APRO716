#!/usr/bin/env python3

multiplier = 0

while multiplier <= 10:
    print(f"Table de {multiplier}: ", end="")

    i = 0
    while i <= 10:
        result = multiplier * i
        print(result, end=" ")
        i += 1

    print()
    multiplier += 1
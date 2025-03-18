#!/usr/bin/env python3

my_array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = [i+2 for i in my_array]
another_array = [i for i in new_array if i > 5]
print(my_array)
print(another_array)
#!/usr/bin/env python3

def remove_duplicate(arr):
    unique_elements = set(arr)
    
    unique_list = list(unique_elements)
    
    return unique_list

original_array = [2, 8, 9, 48, 8, 22, -12, 2]
result = remove_duplicate(original_array)
print(result)
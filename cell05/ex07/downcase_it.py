#!/usr/bin/env python3

import sys

def main():
    if len(sys.argv) != 2:
        print("none")
        return

    input_string = sys.argv[1]
    print(input_string.lower())

if __name__ == "__main__":
    main()
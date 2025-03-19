#!/usr/bin/env python3

import sys
import re

def scan_text(keyword, text):
    matches = re.findall(keyword, text)
    if matches:
        return len(matches)
    else:
        return None

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("none")
    else:
        keyword = sys.argv[1]
        text = sys.argv[2]
        count = scan_text(keyword, text)
        if count is None:
            print("none")
        else:
            print(count)
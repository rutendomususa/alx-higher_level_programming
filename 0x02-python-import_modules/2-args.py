#!/usr/bin/env python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]  # Get arguments, excluding the script name
    num_args = len(argv)
    
    if num_args == 0:
        print(f"{num_args} arguments.")
    elif num_args == 1:
        print(f"{num_args} argument:")
    else:
        print(f"{num_args} arguments:")

    for i, arg in enumerate(argv, 1):
        print(f"{i}: {arg}")

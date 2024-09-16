#!/usr/bin/env python3
import sys  # Import sys to access command-line arguments

if __name__ == "__main__":
    ''' Get all command-line arguments except the script name '''
    argv = sys.argv[1:]
    
    ''' Initialize the total sum to 0 '''
    total = 0

    ''' Loop through the arguments, convert them to integers, and add to total '''
    for arg in argv:
        total += int(arg)
    
    ''' Print the final sum of the arguments '''
    print(total)

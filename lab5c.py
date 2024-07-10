#!/usr/bin/env python3
# Author ID: cdcachero

def add(number1, number2):
    # Add two numbers together, return the result, if error return string 'error: could not add numbers'

    try:
        sum = int(number1) + int(number2)
        return sum

    except ValueError:

        error_msg = 'error: could not add numbers'
        return error_msg
    
def read_file(filename):
    # Read a file, return a list of all lines, if error return string 'error: could not read file'
    
    try:
        f = open(filename,'r')
        read_f = list(f)
        f.close()

        return read_f

    except (FileNotFoundError, PermissionError):
        error_msg = 'error: could not read file'
        return error_msg

if __name__ == '__main__':
    print(add(10,5))                        # works
    print(add('10',5))                      # works
    print(add('abc',5))                     # exception
    print(read_file('seneca2.txt'))         # works
    print(read_file('file10000.txt'))       # exception

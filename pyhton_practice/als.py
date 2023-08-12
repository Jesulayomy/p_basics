"""
    #!usr/bin/env python3
    This module prints all prime numbers
"""

def printn(n: int):
    """ Prints 'n' n times """

    for i in range (n):
        print('n')

if __name__  ==  "__main__":
    import sys
    printn(int(sys.argv[1]))
    
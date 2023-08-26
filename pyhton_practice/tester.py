"""#!/usr/bin/env python3"""
""" Python practice """


def fzbz(n: int):
    """ Fizzbuzz function """

    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)

if __name__ == "__main__":
    import sys
    fzbz(int(sys.argv[1]))

from random import randint
import time
import asyncio


def randn():
    time.sleep(2)
    return(randint(1, 10))

def odds(start, stop):
    """ Prints odd numbers fbetween the given range """

    for i in range(start, stop + 1, 2):
        yield i

def main():
    list_odds = [odd for odd in odds(3, 25)]
    print(list_odds)
    print(randn())
    print([randn() for _ in range(3)])


if __name__ == "__main__":
    main()

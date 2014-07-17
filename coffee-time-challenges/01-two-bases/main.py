#!/usr/bin/env python3

from itertools import combinations_with_replacement


def check(x, y, z):
    return x*100+y*10+z == x+y*9+z*9**2


def main():
    retults = []
    for x, y, z in combinations_with_replacement(list(range(10)), 3):
        if check(x, y, z):
            retults.append((x, y, z))
    return retults

if __name__ == '__main__':
    print(main())

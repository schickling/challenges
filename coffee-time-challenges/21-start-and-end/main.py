#!/usr/bin/env python

from itertools import count, ifilter, islice


def check(number):
    if number % 10 != 6:
        return False
    new_number = int("6" + str(number)[:-1])
    return number*4 == new_number


if __name__ == '__main__':
    print(list(islice(ifilter(check, count(6, 10)), 1))[0])

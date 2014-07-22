#!/usr/bin/env python

"""
This should calculate
46168 * 46465 = 92633 = 2145288753 - 46168 - 46465
"""

from itertools import permutations


def solve_brute_force(numbers):
    """This takes 510,33s. """
    nr_sum = sum(numbers)
    for a, b in permutations(numbers, 2):
        if a*b == nr_sum - a - b:
            return set([a, b])


if __name__ == '__main__':
    numbers = range(1, 65502+1)
    a, b = solve_brute_force(numbers)
    print("{a} * {b} = {absum} = {sum} - {a} - {b}".format(
          a=a, b=b, absum=a+b, sum=sum(numbers)
          ))

#!/usr/bin/env python

"""
This should calculate
46168 * 46465 = 92633 = 2145288753 - 46168 - 46465
"""

from itertools import permutations
import math


def solve_brute_force(numbers):
    """This takes 510,33s. """
    nr_sum = sum(numbers)
    for a, b in permutations(numbers, 2):
        if a*b == nr_sum - a - b:
            return set([a, b])


def solve_better(numbers):
    """This takes 2,74s. """
    nr_sum = sum(numbers)
    for a in sorted(filter(lambda n: n <= math.sqrt(nr_sum), numbers),
                    reverse=True):
        t_sum = nr_sum - a
        b_max = float(t_sum) / a
        b_candidates = sorted(filter(lambda b: b <= b_max, numbers),
                              reverse=True)
        for b in b_candidates:
            if a*b == nr_sum - a - b:
                return set([a, b])

if __name__ == '__main__':
    numbers = range(1, 65502+1)
    a, b = solve_better(numbers)
    print("{a} * {b} = {absum} = {sum} - {a} - {b}".format(
          a=a, b=b, absum=a+b, sum=sum(numbers)
          ))

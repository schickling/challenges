#!/usr/bin/env python

from itertools import product

dice_numbers = list(range(1, 7))
possible_outcomes = list(product(dice_numbers, repeat=3))
possible_sums = map(lambda (a, b, c): a*b*c, possible_outcomes)
odd_sums = filter(lambda n: n % 2 == 1, possible_sums)
print(float(len(odd_sums))/len(possible_outcomes))

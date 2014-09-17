#!/usr/bin/env python

from itertools import permutations

digits = list(range(1, 10))
for down in permutations(digits, 4):
    numerator = sum([10**i * d for i, d in enumerate(down)])
    denominator = 3 * numerator

    # Check if all digits appear exactly once
    d = set(list(str(denominator))).union(set(list(str(numerator))))

    # Print solution
    if 9 == len(d) and ('0' not in d):
        print("%i / %i = 1/3" % (denominator, numerator))

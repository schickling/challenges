#!/usr/bin/env python

from itertools import permutations

digits = list(range(1, 10))
for down in permutations(digits, 4):
    down_number = sum([10**i * d for i, d in enumerate(down)])
    up_number = 3 * down_number
    d = set(list(str(up_number))).union(set(list(str(down_number))))
    if 9 == len(d) and ('0' not in d):
        print("Up number: %i" % up_number)
        print("Down number: %i" % down_number)

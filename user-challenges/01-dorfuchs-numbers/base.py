#!/usr/bin/env python

"""This is the first solution that came to my mind."""

count = 1
for i in range(10**4, 10**5):
    # Get a sorted list of all digits
    l = map(int, sorted(str(i)))

    # Get a list of all neighbored digits as tuples:
    l = zip(l, l[1:])

    # For every digit, check if it is in ascending
    l = map(lambda n: n[0]+1 != n[1], l)

    # Check if all conditions are met
    if any(l):
        continue
    print("%i: %i" % (count, i))
    count += 1

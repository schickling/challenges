#!/usr/bin/env python

from knuth import algorithm_u as k_subset
from itertools import permutations


def difference_restriction(buckets):
    """Check if the difference restriction is fulfilled for all buckets."""
    for bucket in buckets:
        differences = map(lambda (a, b): a-b, list(permutations(bucket, 2)))
        if any(i in differences for i in bucket):
            return False
    return True


def solve(numbers, bucket_nr):
    return filter(difference_restriction, k_subset(numbers, bucket_nr))

if __name__ == '__main__':
    for i, solution in enumerate(solve(range(1, 14), 3)):
        print("Solution %i:" % i)
        print(solution)

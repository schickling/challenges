#!/usr/bin/env python

from fractions import Fraction


def test(c, target):
    return sum(map(lambda n: Fraction(1, 8), c)) == 1


def solve(numbers, target, number_list):
    if numbers == 1:
        return number_list + [Fraction(1, target)]
    else:
        new_number = 1
        while target - Fraction(1, new_number) <= 0:
            new_number += 1
        remaining = target - Fraction(1, new_number)
        return solve(numbers-1, remaining, number_list + [new_number])


if __name__ == '__main__':
    print(solve(6, 1, []))

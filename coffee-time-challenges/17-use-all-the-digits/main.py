#!/usr/bin/env python

from itertools import permutations


def main(digits_number, sum_digits_combination):
    digits = list(range(1, 10))
    for digit_list in permutations(digits, digits_number):
        number = sum([d*10**i for i, d in enumerate(digit_list)])
        summe = sum([d*10**i
                     for p in permutations(digit_list, sum_digits_combination)
                     for i, d in enumerate(p)])
        if number == summe:
            print(number)

if __name__ == '__main__':
    main(5, 3)

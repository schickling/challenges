#!/usr/bin/env python

from itertools import combinations
import locale
# You might have to install the locale
# sudo apt-get install language-pack-de
locale.setlocale(locale.LC_ALL, 'de_DE.utf8')


def get_number(series):
    return sum([10**i * digit for i, digit in enumerate(series)])


def main():
    digits = list(range(10))
    maximum = 0
    maxima = []
    for a in combinations(digits, 4):
        b_digits = sorted(list(set(digits) - set(a)))
        a_number = get_number(a)
        b_number = get_number(b_digits)
        t = a_number * b_number
        if t > maximum:
            maxima = []
        if t >= maximum:
            maximum = t
            maxima.append((a_number, b_number, t))
    return maxima

if __name__ == '__main__':
    maxima = main()
    for a, b, m in maxima:
        print("%i x %i = %s" % (a, b, locale.format("%d", m, grouping=True)))

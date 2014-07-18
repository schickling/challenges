#!/usr/bin/env python3

"""
This solution has a flaw in the order in which arguments get displayed, but
it found the following solution:

   ceil(sqrt(((3!)! * 1) / 2))
 = ceil(sqrt(720/2))
 = ceil(sqrt(360))
 = ceil(18.973)
"""

from itertools import product, permutations, combinations_with_replacement
import operator
import math


def fib(n):
    def accFib(n, Nm2=0, Nm1=1):
        for i in range(n):
            Nm2, Nm1 = Nm1, Nm1+Nm2
        return Nm2   
    return accFib(n)


def identity(n):
    return n


def show_calculation(numbers, binary_ops, unary_ops):
    for i, o in enumerate(unary_ops):
        if o == identity:
            unary_ops[i] = "id"
        elif o == math.sqrt:
            unary_ops[i] = "sqrt"
        elif o == math.factorial:
            unary_ops[i] = "!"
    for i, o in enumerate(binary_ops):
        if o == operator.__add__:
            binary_ops[i] = "+"
        elif o == operator.__truediv__:
            binary_ops[i] = "/"
    return "%s(%s(%s(%s(%i), %s(%i)), %s(%i)))" % (str(unary_ops[4]),
                                                   str(binary_ops[1]),
                                                   str(binary_ops[0]),
                                                   str(unary_ops[0]),
                                                   numbers[0],
                                                   str(unary_ops[1]),
                                                   numbers[1],
                                                   str(unary_ops[2]),
                                                   numbers[2])


def solve(numbers, target):
    mathfunctions = [operator.__add__, operator.__sub__,
                     operator.__truediv__]
    unary_functions = [math.sqrt, identity, math.factorial]
    final_ops = [math.ceil, math.floor]
    solutions = []

    for number_ordered in permutations(numbers):
        number_ordered_s = list(number_ordered)
        for operations in combinations_with_replacement(mathfunctions,
                                                        len(numbers)-1):
            operations = list(operations)
            operations_save = operations[:]
            for unary_applications in product(unary_functions, repeat=5):
                unary_applications = list(unary_applications)
                unary_applications_save = unary_applications[:]
                number_ordered = number_ordered_s
                a, b, c = unary_applications[0:3]
                unary_applications = unary_applications[2:5]
                number_ordered = [a(number_ordered[0]),
                                  b(number_ordered[1]),
                                  c(number_ordered[2])]
                for operation in operations:
                    try:
                        number_ordered_new = [operation(*number_ordered[0:2])]
                    except:
                        break
                    number_ordered_new += number_ordered[2:]
                    number_ordered = number_ordered_new
                    u = unary_applications.pop(0)
                    if number_ordered[0] > 10 and u == math.factorial:
                        break
                    try:
                        number_ordered = ([u(number_ordered[0])] +
                                          number_ordered[1:])
                    except:
                        break
                final = number_ordered[0]
                for final_op in final_ops:
                    final_s = int(final_op(final))
                    if final_s == target:
                        solutions.append(show_calculation(number_ordered_s,
                                                          operations_save,
                                                          unary_applications_save))
    return solutions


if __name__ == '__main__':
    solutions = solve([1, 2, 3], 19)
    print("Solutions:")
    for solution in solutions:
        print(solution)

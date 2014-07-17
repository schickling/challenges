#!/usr/bin/env python

from numpy.linalg import solve


def main(heads, legs):
    """ This kind of task is about solving a linear system of equations with
        x humans, y dogs
        1*x+1*y = heads
        2*x+4*y = legs
    """
    return list(solve([[1, 1], [2, 4]], [heads, legs]))


if __name__ == '__main__':
    humans, dogs = main(72, 200)
    print("There are %i humans and %i dogs." % (humans, dogs))

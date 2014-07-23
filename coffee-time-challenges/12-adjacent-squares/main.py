#!/usr/bin/env python

import math
from itertools import combinations


def is_square(a):
    """Check if a is a perfect square.

    >>> is_square(16)
    True
    >>> is_square(15)
    False
    >>> any(map(is_square, range(200**2+1,201**2-1)))
    False
    """
    root = int(math.sqrt(a))
    return root*root == a


def find_longest_paths(current_node, adjacency_list, path):
    assert current_node in path
    paths = [path]
    for next_node in adjacency_list[current_node]:
        if next_node not in path:
            new_path = path[:]
            new_path.append(next_node)
            new_paths = find_longest_paths(next_node, adjacency_list, new_path)
            if len(new_paths[0]) > len(paths[0]):
                paths = new_paths
            elif len(new_paths[0]) == len(paths[0]):
                paths += new_paths
    return paths


def find_longest_path_in_graph(adjacency_list, verbose=True):
    """Find all longest paths in the graph where each path may not have
       duplicate vertices.
    """
    longest_path_length = 0
    longest_paths = []
    for start_node in adjacency_list.keys():
        paths = find_longest_paths(start_node, adjacency_list, [start_node])
        if len(paths[0]) > longest_path_length:
            longest_path_length = len(paths[0])
            longest_paths = paths
        elif len(paths[0]) == longest_path_length:
            longest_paths += paths
    return longest_paths


def solve(numbers):
    # No repeated numbers please:
    assert len(numbers) == len(set(numbers))

    # Every number is a node and acceptable_neighbors are edges
    # The task is to find the longest path with no repeated nodes

    # I'll do a depth first search on all nodes
    number2index = {}
    for i, number in enumerate(numbers):
        number2index[number] = i

    # Build up data structures
    adjacency_list = {}
    for a, b in combinations(numbers, 2):
        if is_square(a+b):
            if a in adjacency_list:
                adjacency_list[a].append(b)
            else:
                adjacency_list[a] = [b]
            if b in adjacency_list:
                adjacency_list[b].append(a)
            else:
                adjacency_list[b] = [a]

    return find_longest_path_in_graph(adjacency_list)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    paths = solve(list(range(1, 18)))
    for path in paths:
        print(path)

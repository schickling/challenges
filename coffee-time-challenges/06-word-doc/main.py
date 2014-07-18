#!/usr/bin/env python

number_list = [str(i) for i in range(10000+1)]
daughter_list = map(lambda n: n.replace('0', ' '), number_list)
numbers = []
for el in daughter_list:
    for n in el.split(' '):
        if len(n) > 0:
            numbers.append(int(n))
print(sum(numbers))

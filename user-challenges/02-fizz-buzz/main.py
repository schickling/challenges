#!/usr/bin/env python

for i in range(1, 51):
    line = ""
    if i % 3 == 0:
        line += "Fizz"
    if i % 5 == 0:
        line += "Buzz"
    print(line)
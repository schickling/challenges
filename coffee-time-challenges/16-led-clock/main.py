#!/usr/bin/env python

import datetime


def calculate_brighness(time):
    #             0  1  2  3  4  5  6  7  8  9
    brightness = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    summe = 0
    for char in time:
        summe += brightness[int(char)]
    return summe

min_brightnes = calculate_brighness("000")
min_brightnes_time = ["000"]
max_brightnes = calculate_brighness("000")
max_brightnes_time = ["000"]

for i in range(0, 60*24*60, 60):
    display = \
        datetime.datetime.fromtimestamp(
            i
        ).strftime('%H%M')
    if display.startswith("0"):
        display = display[1:]
    brightnes = calculate_brighness(display)

    if min_brightnes > brightnes:
        min_brightnes = brightnes
        min_brightnes_time = [i]
    elif min_brightnes == brightnes:
        min_brightnes_time.append(i)

    if max_brightnes < brightnes:
        max_brightnes = brightnes
        max_brightnes_time = [i]
    elif max_brightnes == brightnes:
        max_brightnes_time.append(i)

print("Min brightness of %i at %s" % (min_brightnes, min_brightnes_time))
print("Max brightness of %i at %s" % (max_brightnes, max_brightnes_time))

a = datetime.datetime.fromtimestamp(float(min_brightnes_time[0]))
b = datetime.datetime.fromtimestamp(float(max_brightnes_time[0]))
print("Time difference: %s" % str(b-a))

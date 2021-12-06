#!/usr/bin/env python3

depth = 0
horiz = 0
position = 0

with open("day2/puzzle1/puzzleinput") as file:
    for element in file.readlines():
        if element.startswith('for') == True:
            horiz += (int(element[-2]))
        if element.startswith('do') == True:
            depth += (int(element[-2]))
        if element.startswith('u') == True:
            depth -= (int(element[-2]))
position = depth * horiz
print(position)

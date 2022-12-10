#!/usr/bin/python3

from itertools import islice

bingopuzzle = []
puzzlerow = []
puzzlevalue = []

#Derives number of total puzzles available
with open("day4/puzzle1/puzzleinput") as file:
    bingoselection = file.readlines()[0].rstrip()

with open("day4/puzzle1/puzzleinput") as file:
    for line in islice(file, 2, None):
        puzzlerow = line.split()

with open ("day4/puzzle1/puzzleinput") as file:
    for line in file:
#        number_of_puzzles = (len(file.readlines() - 2)/5)
         puzzlelength = len(file.readlines())

print(puzzlelength)
numberofpuzzles = int((puzzlelength) / 6)
print(numberofpuzzles)

#with open ("day4/puzzle1/puzzleinput") as file:
#    for puzzle in range(numberofpuzzles):
#        print(puzzle)
#        for i in file:
            #print(i)
#            for row in range(5):
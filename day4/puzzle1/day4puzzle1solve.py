#!/usr/bin/python3

bingoline = []
#Instantiate first line of text file as iterable list of strings
with open("day4/puzzle1/puzzleinput") as file:
    bingoselection = file.readlines()[0].rstrip()
with open("day4/puzzle1/puzzleinput") as file:
    bingopuzzle = file.readlines()
    for line in file:
        for character in line:
            if character != ' ':
                bingoline


#print(bingopuzzle[3])
#Function to convert string to list, separated by commas
def Convert(string):
    li = list(string.split(","))
    return li

def Bingo(string):
    card = list(string.split(" "))
    return card

#print(Convert(bingoselection))
print(Bingo(bingopuzzle[3]))
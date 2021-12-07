#!/usr/bin/python3

from itertools import islice

bingoline = []
#Instantiate first line of text file as iterable list of strings
with open("puzzleinput") as file:
    bingoselection = file.readlines()[0].rstrip()
with open("puzzleinput") as file:
    #bingopuzzle = file.readlines()
    #file_length = len(file.readlines()) - 1
    #number_of_puzzles = int(file_length / 6)
    #puzzlenumber = []
    #puzzleline = []
#Read in each column as a list of strings, then pull out the column values with a loop iterating through list.
    column1 = []
    column2 = []
    column3 = []
    column4 = []
    column5 = []
    linenumber = 1
    #for element in file_length:
        
    for line in islice(file, 2, None):
    #for line in file:
        column1.append(line[:2])
        column2.append(line[3:6])
        column3.append(line[6:9])
        column4.append(line[9:12])
        column5.append(line[12:15])
    column1 = [s.replace('\n', '') for s in column1]
    column1 = column1.remove('')
    print(column1)
    #print(column2)
    #print(column3)
    #print(puzzleline)
    #print(file_length)
    #print(number_of_puzzles)
#    print(line)

#print(bingopuzzle[3])
#Function to convert string to list, separated by commas
def Convert(string):
    li = list(string.split(","))
    return li

def Bingo(string):
    card = list(string.split(" "))
    return card


#print(Convert(bingoselection))
#print(Bingo(bingopuzzle[3]))
#try this: https://stackoverflow.com/questions/15963959/reading-a-line-of-integers-in-python

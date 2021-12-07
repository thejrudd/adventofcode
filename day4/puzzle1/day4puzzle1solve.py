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
    row_dict1 = {}
    row_dict2 = {}
    row_dict3 = {}
    row_dict4 = {}
    row_dict5 = {}
    linenumber = 1
    #for element in file_length:
        
    for line in islice(file, 2, None):
# Creates lists of the input of each column, as two character strings.
        column1.append(line[:2])
        column2.append(line[3:6])
        column3.append(line[6:9])
        column4.append(line[9:12])
        column5.append(line[12:15])
# Replaces new line list entries with blank space.
    column1 = [s.replace('\n', '') for s in column1]
# Deletes blank space '' entries in list    
    del column1[5::6]
    del column2[5::6]
    del column3[5::6]
    del column4[5::6]
    del column5[5::6]
# Reads in column string entries and converts them to integer values
    for entry in range(0, len(column1)):
        column1[entry] = int(column1[entry])
        column2[entry] = int(column2[entry])
        column3[entry] = int(column3[entry])
        column4[entry] = int(column4[entry])
        column5[entry] = int(column5[entry])
# Creates dictionary where key = row number and value = column entry
    for row_number in range(0, len(column1)):
        row_dict1[row_number] = column1[row_number]
        row_dict2[row_number] = column1[row_number]
        row_dict3[row_number] = column1[row_number]
        row_dict4[row_number] = column1[row_number]
        row_dict5[row_number] = column1[row_number]
print(len(column4))
# Resolves which puzzle number we are working on by dividing total rows by 5.
    #print(column1)
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

#!/usr/bin/env python3

calories1 = 0
calories2 = 0
caloriesmax = 0
linecounter = 0

with open('C:\\Users\\jruddick\\Documents\\GitHub\\adventofcode\\2022\\Day 1\\puzzle input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        if line.isnumeric():
            print(line)
        else:
            print(f"{line} is not numeric.")

        
                
            
            

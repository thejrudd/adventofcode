import re

overlap = 0
total = 0

# Opens puzzle input file and reads through it line by line until the file finishes.
with open('/Users/justinruddick/Documents/GitHub/adventofcode/2022/Day 4/puzzleinput.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        # Removes the "new line" character from the end of each line, finds the length of each line, then creates a string for each half of each line.
        line = line.strip()
        valuelist = re.split("-|,|\+", line)
        if int(valuelist[0]) >= int(valuelist[2]):
            if int(valuelist[1]) < int(valuelist[3]):
                total += 1
        else:
            if int(valuelist[0]) <= int(valuelist[2]):
                if int(valuelist[1]) > int(valuelist[3]):
                #  print(valuelist[0] + " " + valuelist[2])
                # print(valuelist[1] + " " + valuelist[3])
                    total += 1
    print(total)
            
            
        


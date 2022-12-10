length = 0
compartment1 = 0
compartment2 = 0
lowalphabet = dict()
upalphabet = dict()
priority = 0
total = 0

# Initializes lower case alphabet as dictionary with the letter of the alphabet as key, and its position in the alphabet as value.
for lowletter in "abcdefghijklmnopqrstuvwxyz":
    lowalphabet[lowletter] = ord(lowletter) - ord("a") + 1

# Doing the same for the upper case alphabet, except with values +26
for upletter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    upalphabet[upletter] = ord(upletter) - ord("A") + 27

# Opens puzzle input file and reads through it line by line until the file finishes.
with open('/Users/justinruddick/Documents/GitHub/adventofcode/2022/Day 3/puzzleinput.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        # Removes the "new line" character from the end of each line, finds the length of each line, then creates a string for each half of each line.
        line = line.strip()
        length = len(line)
        compartment1 = line[:length//2]
        compartment2 = line[length//2:]
        # Creates a set of values generated from each string, then finds the values that are shared in each set.
        set1 = set(compartment1)
        set2 = set(compartment2)
        intersection = set1 & set2
        # Converts the intersecting values into a string, then finds the corresponding key in each dictionary defined earlier, and outputs its value.
        intersection = ", ".join(intersection)
        if str(intersection) in lowalphabet:
            priority = lowalphabet[intersection]
        else:
            if str(intersection) in upalphabet:
                priority = upalphabet[intersection]
        # Adds the "priority" of this line to the current running total.
        total = total + priority
print(total)

            
        


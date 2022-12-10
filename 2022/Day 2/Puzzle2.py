rock = 1
paper = 2
scissors = 3
score = 0
total = 0

with open('/Users/justinruddick/Documents/GitHub/adventofcode/2022/Day 2/puzzle input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        # total = score + total
        # score = 0
        line = line.strip()
        line = line.split(" ")
        firstchar = str(line[0])
        secondchar = str(line[1])
        # print(secondchar)
        # print(firstchar)
        if secondchar == "X":
            # print("rock")
            score = rock
            if firstchar == "A":
                score = score + 3
                # print("draw")
            elif firstchar == "B":
                # print("loss")
                score = score + 0             
            elif firstchar == "C":
                score = score + 6
                # print("win")
        else:
            if secondchar == "Y":
                score = paper
                # print ("paper")
                if firstchar == "A":
                    score = score + 6
                elif firstchar == "B":
                    score = score + 3
                elif firstchar == "C":
                    score = score + 0
            else:
                if secondchar == "Z":
                    score = scissors
                    # print("scissors")
                    if firstchar == "A":
                        score = score + 0
                    elif firstchar == "B":
                        score = score + 6
                    elif firstchar == "C":
                        score = score + 3
        total = score + total
    print(total)
        
   

        
                
            
            
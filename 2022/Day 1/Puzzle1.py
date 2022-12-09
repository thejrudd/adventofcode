caloriestest = 0
caloriesmax = 0

with open('C:\\Users\\jruddick\\Documents\\GitHub\\adventofcode\\2022\\Day 1\\puzzle input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        if not line:
            if caloriestest > caloriesmax:
                caloriesmax = caloriestest
            caloriestest = 0
        else:
            caloriestest = int(line) + caloriestest
    print(caloriesmax)
        
   

        
                
            
            
#!/usr/bin/env python3

position1 = []
position2 = []
position3=  []
position4 = []
position5 = []
position6 = []
position7 = []
position8 = []
position9 = []
position10 = []
position11 = []
position12 = []
sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0
sum5 = 0
sum6 = 0
sum7 = 0
sum8 = 0
sum9 = 0
sum10 = 0
sum11 = 0
sum12 = 0

with open("puzzleinput") as file:
    for element in file.readlines():
        position1.append(element[0])
        position2.append(element[1])
        position3.append(element[2])
        position4.append(element[3])
        position5.append(element[4])
        position6.append(element[5])
        position7.append(element[6])
        position8.append(element[7])
        position9.append(element[8])
        position10.append(element[9])
        position11.append(element[10])
        position12.append(element[11])

for item in position1:
    sum1 = int(item) + sum1
if sum1 < ((len(position1)/2)):
    gamma1 = 0
    epsilon1 = 1
else:
    gamma1 = 1
    epsilon1 = 0

for item in position2:
    sum2 = int(item) + sum2
if sum2 < ((len(position2)/2)):
    gamma2 = 0
    epsilon2 = 1
else:
    gamma2 = 1
    epsilon2 = 0

for item in position3:
    sum3 = int(item) + sum3
if sum3 < ((len(position3)/2)):
    gamma3 = 0
    epsilon3 = 1
else:
    gamma3 = 1
    epsilon3 = 0

for item in position4:
    sum4 = int(item) + sum
if sum4 < ((len(position4)/2)):                                                                        │jruddick@JRUDDICK-ZBX:~/teaching-sand-to-think/advent/day3/puzzle1$ ./day3puzzle1solve.py
    gamma4 = 0                                                                                         │1000
    epsilon4 = 1                                                                                       │487
else:                                                                                                  │0
    gamma4 = 1                                                                                         │jruddick@JRUDDICK-ZBX:~/teaching-sand-to-think/advent/day3/puzzle1$
    epsilon4 = 0

for item in position5:                                                                                 │0
    sum5 = int(item) + sum5                                                                            │jruddick@JRUDDICK-ZBX:~/teaching-sand-to-think/advent/day3/puzzle1$
if sum5 < ((len(position5)/2)):                                                                        │jruddick@JRUDDICK-ZBX:~/teaching-sand-to-think/advent/day3/puzzle1$ ./day3puzzle1solve.py
    gamma5 = 0                                                                                         │1000
    epsilon5 = 1                                                                                       │487
else:                                                                                                  │0
    gamma5 = 1                                                                                         │jruddick@JRUDDICK-ZBX:~/teaching-sand-to-think/advent/day3/puzzle1$
    epsilon5 = 0

for item in position6:                                                                                 │0
    sum6 = int(item) + sum6                                                                            │jruddick@JRUDDICK-ZBX:~/teaching-sand-to-think/advent/day3/puzzle1$
if sum6 < ((len(position6)/2)):                                                                        │jruddick@JRUDDICK-ZBX:~/teaching-sand-to-think/advent/day3/puzzle1$ ./day3puzzle1solve.py
    gamma6 = 0                                                                                         │1000
    epsilon6 = 1                                                                                       │487
else:                                                                                                  │0
    gamma6 = 1                                                                                         │jruddick@JRUDDICK-ZBX:~/teaching-sand-to-think/advent/day3/puzzle1$
    epsilon6 = 0

for item in position7:                                                                                 │0
    sum7 = int(item) + sum7                                                                            │jruddick@JRUDDICK-ZBX:~/teaching-sand-to-think/advent/day3/puzzle1$
if sum7 < ((len(position7)/2)):                                                                        │jruddick@JRUDDICK-ZBX:~/teaching-sand-to-think/advent/day3/puzzle1$ ./day3puzzle1solve.py
    gamma7 = 0                                                                                         │1000
    epsilon7 = 1                                                                                       │487
else:                                                                                                  │0
    gamma7 = 1                                                                                         │jruddick@JRUDDICK-ZBX:~/teaching-sand-to-think/advent/day3/puzzle1$
    epsilon7 = 0

for item in position8:                                                                                 │0
    sum8 = int(item) + sum8                                                                            │jruddick@JRUDDICK-ZBX:~/teaching-sand-to-think/advent/day3/puzzle1$
if sum8 < ((len(position8)/2)):                                                                        │jruddick@JRUDDICK-ZBX:~/teaching-sand-to-think/advent/day3/puzzle1$ ./day3puzzle1solve.py
    gamma8 = 0                                                                                         │1000
    epsilon8 = 1                                                                                       │487
else:                                                                                                  │0
    gamma8 = 1                                                                                         │jruddick@JRUDDICK-ZBX:~/teaching-sand-to-think/advent/day3/puzzle1$
    epsilon8 = 0

for item in position9:                                                                                 │0
    sum9 = int(item) + sum9                                                                            │jruddick@JRUDDICK-ZBX:~/teaching-sand-to-think/advent/day3/puzzle1$
if sum9 < ((len(position9)/2)):                                                                        │jruddick@JRUDDICK-ZBX:~/teaching-sand-to-think/advent/day3/puzzle1$ ./day3puzzle1solve.py
    gamma9 = 0                                                                                         │1000
    epsilon9 = 1                                                                                       │487
else:                                                                                                  │0
    gamma9 = 1                                                                                         │jruddick@JRUDDICK-ZBX:~/teaching-sand-to-think/advent/day3/puzzle1$
    epsilon9 = 0

for item in position10:                                                                                 │0
    sum10 = int(item) + sum10
if sum10 < ((len(position10)/2)):                                                                        │jruddick@JRUDDICK-ZBX:~/teaching-sand-to-think/advent/day3/puzzle1$ ./day3puzzle1solve.py
    gamma10 = 0                                                                                         │1000
    epsilon10 = 1                                                                                       │487
else:                                                                                                  │0
    gamma10 = 1                                                                                         │jruddick@JRUDDICK-ZBX:~/teaching-sand-to-think/advent/day3/puzzle1$
    epsilon10 = 0

for item in position11:                                                                                 │0
    sum11 = int(item) + sum11                                                                            │jruddick@JRUDDICK-ZBX:~/teaching-sand-to-think/advent/day3/puzzle1$
if sum11 < ((len(position11)/2)):                                                                        │jruddick@JRUDDICK-ZBX:~/teaching-sand-to-think/advent/day3/puzzle1$ ./day3puzzle1solve.py
    gamma11 = 0                                                                                         │1000
    epsilon11 = 1                                                                                       │487
else:                                                                                                  │0
    gamma11 = 1                                                                                         │jruddick@JRUDDICK-ZBX:~/teaching-sand-to-think/advent/day3/puzzle1$
    epsilon11 = 0

for item in position12:                                                                                 │0
    sum12 = int(item) + sum12                                                                           │jruddick@JRUDDICK-ZBX:~/teaching-sand-to-think/advent/day3/puzzle1$
if sum12 < ((len(position12)/2)):                                                                        │jruddick@JRUDDICK-ZBX:~/teaching-sand-to-think/advent/day3/puzzle1$ ./day3puzzle1solve.py
    gamma12 = 0                                                                                         │1000
    epsilon12 = 1                                                                                       │487
else:                                                                                                  │0
    gamma12 = 1                                                                                         │jruddick@JRUDDICK-ZBX:~/teaching-sand-to-think/advent/day3/puzzle1$
    epsilon12 = 0

gammalist = [
gamma1, 
gamma2, 
gamma3, 
gamma4, 
gamma5, 
gamma6, 
gamma7, 
gamma8, 
gamma9, 
gamma10, 
gamma11, 
gamma12
]
print(gammalist)

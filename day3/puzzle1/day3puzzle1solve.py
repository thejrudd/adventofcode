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

with open("day3/puzzle1/puzzleinput") as file:
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
    sum4 = int(item) + sum4
if sum4 < ((len(position4)/2)):
    gamma4 = 0
    epsilon4 = 1
else:         
    gamma4 = 1
    epsilon4 = 0

for item in position5:
    sum5 = int(item) + sum5
if sum5 < ((len(position5)/2)):
    gamma5 = 0             
    epsilon5 = 1           
else:                      
    gamma5 = 1             
    epsilon5 = 0

for item in position6:     
    sum6 = int(item) + sum6
if sum6 < ((len(position6)/2)):
    gamma6 = 0                 
    epsilon6 = 1                
else:                           
    gamma6 = 1                  
    epsilon6 = 0

for item in position7:          
    sum7 = int(item) + sum7     
if sum7 < ((len(position7)/2)): 
    gamma7 = 0                  
    epsilon7 = 1                
else:                           
    gamma7 = 1                  
    epsilon7 = 0

for item in position8:
    sum8 = int(item) + sum8              
    
if sum8 < ((len(position8)/2)):          
    gamma8 = 0                           
    epsilon8 = 1                         
else:                                    
    gamma8 = 1                           
    epsilon8 = 0

for item in position9:                   
    sum9 = int(item) + sum9              
if sum9 < ((len(position9)/2)):          
    gamma9 = 0                           
    epsilon9 = 1                         
else:                                    
    gamma9 = 1                           
    epsilon9 = 0

for item in position10:                  
    sum10 = int(item) + sum10
if sum10 < ((len(position10)/2)):        
    gamma10 = 0                          
    epsilon10 = 1                        
else:                                    
    gamma10 = 1                          
    epsilon10 = 0

for item in position11:                  
    sum11 = int(item) + sum11            
if sum11 < ((len(position11)/2)):        
    gamma11 = 0                          
    epsilon11 = 1                        
else:                                    
    gamma11 = 1                          
    epsilon11 = 0

for item in position12:                  
    sum12 = int(item) + sum12            
if sum12 < ((len(position12)/2)):        
    gamma12 = 0                          
    epsilon12 = 1                        
else:                                    
    gamma12 = 1                          
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
epsilonlist = [
    epsilon1, 
    epsilon2, 
    epsilon3, 
    epsilon4, 
    epsilon5, 
    epsilon6, 
    epsilon7, 
    epsilon8, 
    epsilon9, 
    epsilon10, 
    epsilon11, 
    epsilon12
]

gammastringlist = [str(i) for i in gammalist]
gammavalue = int("".join(gammastringlist))
gammastringnew = str(gammavalue)
gammaint = int(gammastringnew, 2)

epsilonstringlist = [str(i) for i in epsilonlist]
epsilonvalue = int("".join(epsilonstringlist))
epsilonstringnew = str(epsilonvalue)
epsilonint = int(epsilonstringnew, 2)

print(gammaint)
print(epsilonint)

print(gammaint * epsilonint)

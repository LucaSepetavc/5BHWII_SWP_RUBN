import random

rafflenumbers = [] 
for x in range(45): 
    rafflenumbers.append(x+1) 

random.shuffle(rafflenumbers)


for x in range(6): 
    print(rafflenumbers[x])
    
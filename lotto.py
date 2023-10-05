import random
import matplotlib.pyplot as plt


selectedNumber = []

numbers = [] 
results = {}

  
def draw(aufrufe, numbers):
    i = 44 - aufrufe
    index = random.randint(0,i) 
    
    randomNumber = numbers[index]
    numbers[index] = numbers[i]
    numbers[i] = randomNumber
    selectedNumber.append(randomNumber)
    
    old = results.get(randomNumber)
    
    results[randomNumber] = old + 1
    

for x in range(45):
    x = x+1 
    results[x] = 0
    numbers.append(x)
    
             
for f in range(1000):
    for i in range(6):
        draw(i, numbers)

print(results)

plt.bar(results.keys(), results.values())
plt.show()

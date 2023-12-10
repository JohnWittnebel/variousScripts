import numpy
import random

ROLLS = 28080
RARITIES = [2, 5, 10, 20]
QUANTITIES = [2, 4, 14, 111]

def singleTrial():
    foundArr = numpy.zeros(QUANTITIES[0] + QUANTITIES[1] + QUANTITIES[2] + QUANTITIES[3])
    foundAll = False
    numRolls = 0

    while not foundAll:
        # generate new item, see if it is a unique
        numRolls += 1
        newItem = random.randint(1,ROLLS)
        currInd = 0
        foundItem = False
        for i in range(len(RARITIES)):
            for _ in range(QUANTITIES[i]):
                if newItem <= RARITIES[i]:
                    foundArr[currInd] += 1
                    foundItem = True
                    break
                else:
                    newItem -= RARITIES[i]
                currInd += 1
            if foundItem:
                break
    
        # check if all items have been found
        foundAll = True
        for ele in foundArr:
            if ele == 0:
                foundAll = False
            
    return numRolls

sumTotal = 0
for _ in range(100):
    sumTotal += singleTrial()

print(sumTotal / 100)
print(sumTotal / 300)
   

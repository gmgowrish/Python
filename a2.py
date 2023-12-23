# fill a 1d array with random values , then print them,one per line
from array import array
import random

valueList = array('i', [0] * 1)  # the array size for 0 to 100

# fill the array with random floating point values

for i in range(len(valueList)):
    valueList[i] = random.randint(0, 5)  # (elements)for creating the random number for 0 to 5

for value in valueList:
    print(value)

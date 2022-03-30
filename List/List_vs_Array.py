import numpy as np

myArray = np.array([1,2,3,4,5,6,"a"])
myList = [1,2,3,4,5,6,"a"]

print(myArray) # Converting all values to the string.
print(myList) # Working good.

myArray = np.array([1,2,3,4,5,6])
myList = [1,2,3,4,5,6]

print(myArray/2) # Working good.
print(myList/2) # Giving error.


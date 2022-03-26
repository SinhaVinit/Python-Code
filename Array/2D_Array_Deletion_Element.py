import numpy as np

twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
print(twoDArray)

newTwoDArray = np.delete(twoDArray, 0, axis=0)
print(newTwoDArray)

newTwoDArray = np.delete(twoDArray, 0, axis=1)
print(newTwoDArray)

newTwoDArray = np.delete(twoDArray, 1, axis=0)
print(newTwoDArray)

newTwoDArray = np.delete(twoDArray, 1, axis=1)
print(newTwoDArray)
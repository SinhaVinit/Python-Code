from array import *

arr1 = array("i", [1,2,3,4,5,6])
arr2 = array("d", [1.2, 1.3, 1.4, 1.5])

def traverseArray(array):
    for i in array:
        print(i)

traverseArray(arr1)
print("---------------------")
traverseArray(arr2)
from array import *

arr1 = array("i", [1,2,3,4,5,6])
arr2 = array("d", [1.2, 1.3, 1.4, 1.5])

arr1.insert(6,7)
arr2.insert(4, 1.6)

print(arr1)
print(arr2)

arr1.insert(0,0)
arr2.insert(0, 1.1)

print(arr1)
print(arr2)

arr1.insert(2,10)
arr2.insert(2, 2.0)

print(arr1)
print(arr2)
from array import *

# 1. Create an array and traverse.
print("Step 1")
my_array = array("i", [1,2,4,5,6,7,8,9,10])
for i in my_array:
    print(i)

# 2. Access individual elements through indexes.
print("Step 2")
print(my_array[4])

# 3. Append any value to the array using append() method.
print("Step 3")
my_array.append(11)
print(my_array)

# 4. Insert value in an array using insert() method
print("Step 4")
my_array.insert(2, 3)
print(my_array)

# 5. Extend python array using extend() method
print("Step 5")
my_array2 = array("i", [12,13,14,15])
my_array.extend(my_array2)
print(my_array)

# 6. Add items from list into array using fromlist() method
print("Step 6")
tempList = [16,17,18,19,20]
my_array.fromlist(tempList)
print(my_array)

# 7. Remove any array element using remove() method
print("Step 7")
my_array.remove(20) # If multiple 20 is there then, it will remove only the first comming 20 from the array.
print(my_array)

# 8. Remove last array element using pop() method
print("Step 8")
my_array.pop()
print(my_array)

# 9. Fetch any element through its index using index() method
print("Step 9")
print(my_array.index(11))

# 10. Reverse a python array using reverse() method
print("Step 10")
my_array.reverse()
print(my_array)

# 11. Get array buffer information through buffer_info() method
print("Step 11")
print(my_array.buffer_info())

# 12. Check for number of occurrences of an element using count() method
print("Step 12")
my_array.append(11)
print(my_array)
print(my_array.count(11))

# 13. Convert array to string using tostring() method
print("Step 13")
strTemp = my_array.tobytes()
print(strTemp)
strNew = array("i")
strNew.frombytes(strTemp)
print(strNew)

# 14. Convert array to a python list with same elements using tolist() method
print("Step 14")
print(my_array.tolist())

# 15. Append a string to char array using fromstring() method
# print("Step 15")
# newStr = "Hello"
# newArr = array("")
# newArr.frombytes(newStr)
# print(newArr)

# 16. Slice Elements from an array
print("Step 16")
print(my_array[1:4])
print(my_array[:4])
print(my_array[1:])
print(my_array[:])
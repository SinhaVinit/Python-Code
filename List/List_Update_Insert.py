myList = [1,2,3,4,5,6,7,8,9,10]
print(myList)

# # Updating list...........
# myList[2] = 33
# myList[3] = 44
# print(myList)

# Inserting element into the list........
# insert()
myList.insert(0,11)
print(myList)
myList.insert(5,15)
print(myList)
# append()
myList.append(100)
print(myList)
# extend()
newList = [200,300,400,500]
myList.extend(newList)
print(myList)
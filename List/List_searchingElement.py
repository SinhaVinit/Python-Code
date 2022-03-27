myList = [1,2,3,4,5,6,7,8,9,10]
print(myList)

# "in" operator
if 4 in myList:
    print(myList.index(4))
else:
    print("The value does not exist in the list!")

# Linear Search
def searchinList(list, value):
    for i in list:
        if i == value:
            return list.index(value)
    return "The value does not exist in the list!"

print(searchinList(myList, 6))
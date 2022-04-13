newTuple = ("a", "b", "c", "d", "e")

# print("b" in newTuple)
# print("f" in newTuple)

def searchTuple(pTuple, element):
    for i in pTuple: #-------------------------------> O(n)
        if i == element: #---------------------------> O(1)
            return pTuple.index(i) #-----------------> O(1)
    return "The element does not exist." #-----------> O(1)

print(searchTuple(newTuple, "c"))
print(searchTuple(newTuple, "f"))

# Time Complexity: O(n)
# Space Complexity: O(1)
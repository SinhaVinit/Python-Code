myDict = {"name": "Vinit", "age": 22, "address": "Kolkata,India", "education": "phd"}

# print(myDict.pop("age"))
# print(myDict)

# print(myDict.popitem())
# print(myDict)

# myDict.clear()
# print(myDict)

# del myDict["age"]
# print(myDict)

del myDict
# print(myDict) # This will give an error because the dictionary was deleted

# Time Complexity: O(1) or amortized O(n)
# Space Complexity: O(1)
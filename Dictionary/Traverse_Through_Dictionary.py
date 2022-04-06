myDict = {"name": "Vinit", "age": 22, "address": "Kolkata,India"}

def traverseDict(dict):
    for key in dict:    #----------------------------------------> Time Complexity: O(n)
        print(key, dict[key])    #-------------------------------> Time Complexity: O(1)

traverseDict(myDict)

# Time Complexity: O(n)
# Space Complexity: O(1)
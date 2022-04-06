myDict = {"name": "Vinit", "age": 22, "address": "Kolkata,India"}

def searchDict(dict,value):
    for key in dict:    #-------------------------------------------------> Time Complexity: O(n)
        if dict[key] == value:    #---------------------------------------> Time Complexity: O(1)
            return key, value    #----------------------------------------> Time Complexity: O(1)
    return "The value does not exist."    #-------------------------------> Time Complexity: O(1)

print(searchDict(myDict, "Vinit"))
print(searchDict(myDict, "Hello"))

# Time Complexity: O(n)
# Space Complexity: O(1)
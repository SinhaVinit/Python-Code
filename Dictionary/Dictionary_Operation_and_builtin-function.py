from textwrap import shorten
from typing import KeysView

from numpy import short, triu


myDict = {"one": 1, "two": 2, "three": 3, "four": 4}

# print("one" in myDict) # --------------------------> Time Complexity: O(1), Space Complexity: O(1)

# print(1 in myDict.values()) # ---------------------> Time Complexity: O(1), Space Complexity: O(1)

# for key in myDict: # --------------------------------> Time Complexity: O(n), Space Complexity: O(1)
#     print(key, myDict[key]) # -----------------------> Time Complexity: O(1), Space Complexity: O(1)

# newDict = {1: True, 2: True}
# print(all(newDict))
# newDict = {1: "True", 2: "True"}
# print(all(newDict))
# newDict = {0: False, 1: False}
# print(all(newDict))
# newDict = {0: True, 1: False, 2: False}
# print(all(newDict))
# newDict = {0: False, 1: True, 2: True}
# print(all(newDict))
# newDict = {}
# print(all(newDict))

# newDict = {1: True, 2: True}
# print(any(newDict))
# newDict = {1: "True", 2: "True"}
# print(any(newDict))
# newDict = {0: False}
# print(any(newDict))
# newDict = {0: True, 1: False, 2: False}
# print(any(newDict))
# newDict = {0: False, 1: True, 2: True}
# print(any(newDict))
# newDict = {}
# print(any(newDict))

# myDict = {"one": 1, "two": 2, "three": 3, "four": 4}
# print(len(myDict))

myDict = {"e": 1, "a": 2, "i": 3, "u": 4, "o": 5}
print(sorted(myDict))
print(sorted(myDict, reverse=True))
newDict = {"evds": 1, "aaf": 2, "ai": 3, "dfasdu": 4, "fadsfadsfo": 5}
print(sorted(newDict, key=len))
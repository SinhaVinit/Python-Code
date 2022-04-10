newTuple1 = "a", "b", "c", "d", "e"
print(newTuple1)

newTuple2 = ("a", "b", "c", "d", "e")
print(newTuple2)

newTuple3 = ("a",) # This will be treated as Tuple because there is "," after a.
print(newTuple3)

newTuple4 = ("a") # This will be treated as string because there is no "," after a.
print(newTuple4)

newTuple5 = tuple()
print(newTuple5)

newTuple5 = tuple("abcde")
print(newTuple5)

# Time Complexity: O(1)
# Space Complexity: O(n)
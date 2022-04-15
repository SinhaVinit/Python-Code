# List is mutable, whereas a tuple is immutable
list1 = [0,1,2,3,4,5,6,7,8]
list1[1] = 3
print(list1)

list1 = [8,7,6,5,4,3,2,1,0]
print(list1)

del list1[0]
print(list1)

#--------------------

tuple1 = (0,1,2,3,4,5,6,7,8)
# tuple[1] = 3

tuple1 = (8,7,6,5,4,3,2,1,0)
print(tuple1)

# del tuple1[0]
print(tuple1)

# Function that can be used for both lists and tuples: len(), max(), min(), sum(), any(), all(), sorted().
# Methods that can be used for both lists and tuples: count(), index()

# Method for lists only: append(), insert(), remove(), pop(), clear(), sort(), reverse()

# Tuple can be stored in Lists.
# Lists can be stored in Tuples.
list1 = [(1,2), (9,0), (3,4)]
tuple1 = ([1,2], [3,4], [5,6])
print(list1)
print(tuple1)

# Both tuples and lists can be nested.
list1 = [[1,2], [9,0], [3,4]]
tuple1 = ((1,2), (3,4), (5,6))
print(list1)
print(tuple1)

# -> We generally use tuples for heterogeneous (different) data types and lists for homogeneous (similar) data types.
# -> Iteration through a tuple is faster than with list.
# -> Tuples that contain immutable elements can be used as a key for a dictionary.
# -> If you have data that doesn't change, implementing it as tuple will guarantee that it remains write-protected.
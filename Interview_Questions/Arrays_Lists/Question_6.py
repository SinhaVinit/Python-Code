# Permutaion

def permutation(list1, list2):
    if len(list1) != len(list2):
        return False
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    return False

list1 = [1,2,3,4]
list2 = [2,1,4,3]
print(permutation(list1, list2))

list1 = [1,2,3,4]
list2 = [2,1,5,3]
print(permutation(list1, list2))

list1 = ['a','b','c','d']
list2 = ['b','a','d','c']
print(permutation(list1, list2))

list1 = ['a','b','c','d']
list2 = ['b','a','e','c']
print(permutation(list1, list2))


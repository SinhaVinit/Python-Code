# Pair / two sum - LeetCode 1
# Write a orograme to find all pairs of integers whose sum is equal to a given number.
# Ex: [2,6,3,9,11] 9 ----> [6,3]

# Does array contains only positive or negative numbers?
# What if the same pairs repeate twice, should we print it every time?
# If the reverse of the pair is acceptable e.g. can we print both [4,1] and [1,4] if given sum is 5.
# Does we need to print only distinct pairs? does [3,3] is a valid pair forgiven sum of 6?
# How big is the array?

def findPairs(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                continue
            elif nums[i] + nums[j] == target:
                print(i, j)

myList = [1,2,3,2,3,4,5,6]
findPairs(myList, 6)
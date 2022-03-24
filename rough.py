def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)):
        for j in range(len(nums)-1):
            if nums[i]+nums[j+1] == target:
                lst = [i, j+1]
                return lst

print(twoSum([1,2,3,4,5,6,7,8,9.10], 5))
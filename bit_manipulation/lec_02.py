def findSingle(nums):
    res = 0
    for ele in nums:
        res = res ^ ele
    
    return res


nums = [2, 3, 4, 5, 2, 5, 4]

print(findSingle(nums))
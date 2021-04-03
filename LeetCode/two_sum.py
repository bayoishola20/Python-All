# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# TWO SUM

class Solution:
    def twoSum(self, nums, target):
        total = {}
        for i, num in enumerate(nums):              # enumerate each item in nums
            n = (target - num)                      # difference of target and each element in nums
            if n not in total:                      # if difference value is not in total, append item in nums as key and its index as the value
                total[num] = i                      
            else:
                return [ total[n], i]               # otherwise, return the index of the difference in total and the other

a = Solution()

# Test 1
print(a.twoSum([3,2,4], 6)) # [1, 2]

# Test 2
print(a.twoSum([2,7,11,15], 9)) # [0, 1]

# Test 2
print(a.twoSum([3, 3], 6)) # [0, 1]
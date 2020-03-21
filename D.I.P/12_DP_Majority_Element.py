# A majority element is an element that appears more than half the time.
# Given a list with a majority element, find the majority element.

def majority_element(nums):
    unique_elements = set(nums)                                     # get the unique elements
    freq = nums.count                                               # gets count of each item
    return max(unique_elements, key=freq)                           # returns the maximum occurence. "Key" is a lambda function that compares integer version of each item of unique elements in nums count.


print majority_element([3, 5, 3, 3, 2, 4, 3])
# 3
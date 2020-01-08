# You are given a list of numbers, and a target number k. Return whether or not there are two numbers in the list that add up to k.

def two_sum(numList, k):
  for i in range(0, len(numList)):
      end = len(numList) - 1
      if numList[0] + end == k:
          pass

print two_sum([4,7,1,-3,2], 5)
# return True since 4 + 1 = 5.
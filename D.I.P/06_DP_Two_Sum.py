# You are given a list of numbers, and a target number k. Return whether or not there are two numbers in the list that add up to k.

def two_sum(numList, k):
    s = set() # a set to store unique elements
    for i in range(0, len(numList)): # loop through the numList
        diff = k - numList[i] # get difference of k and each element
        s.add(numList[i]) # add all items in numList to set s

        if (diff in s): # if the diff is in the set s
            #print str(diff), str(numList[i]) #print the diff calculated that is found in s and the numList item that sums up to k 
            return True
        

print two_sum([4,7,1,-3,2], 5)
# return True since 4 + 1 = 5.
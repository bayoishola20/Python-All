'''
Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].

'''

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    B = []
    
    for i in A:
        if i > 0:
            B.append(i)
    B = sorted(B)
    
    if 1 not in B:
        return 1

    for i in range(0, len(B)-1):
        if (B[i+1] - B[i]) > 1:
            return B[i] + 1
    return max(B) + 1
    
    #pass
# The power function calculates x raised to the nth power. 
# If implemented in O(n) it would simply be a for loop over n and multiply x n times. 
# Instead implement this power function in O(log n) time. You can assume that n will be a non-negative integer.


def pow(x, n):
    if n == 1:
        return x
    else:
        return x * pow(x, n-1)

print(pow(5, 3))
# 125
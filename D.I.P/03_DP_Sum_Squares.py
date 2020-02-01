# Given a number n, find the least number of squares needed to sum up to the number.

def square_sum(n):
    # minimum squares for 3, 2 and 1 is same as the number itself. Check by solving.
    if n <= 3:
        return n
    # check if number is a perfect square return 1
    elif n == int( pow(n,1/2) ):
        return 1
    
    ans = n # store maximum squares needed

    for i in range(1, n+1):
        tmp = i * i
        if tmp > n:
            break
        elif tmp == n:
            ans = 1
        else:
            ans = min( ans, 1 + square_sum(n - tmp) ) # recursion
    return ans

print square_sum(100)
# Min sum is 3^2 + 2^2
# 2

#PS: This solution works for small values of n.
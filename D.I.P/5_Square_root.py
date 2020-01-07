# Given a positive integer, find the square root of the integer without using any built in square root or power functions (math.sqrt or the ** operator). Give accuracy up to 3 decimal points.

def sqrt(x):
    if (x == 1 or x == 0):
        return x
    
    start = 0
    end = x
    mid = 0.0
    while ( (end - start) > 0.001):
        mid = (start + end) / 2.0 # find middle value and as a float
        # print mid

        if ( abs(mid * mid - x) <= 0.001):
            return mid
        
        if (mid * mid < x):
            start = mid
        
        # else if mid * mid > x
        else:
            end = mid
    return format(mid, ".3f") # format to 3 d.p
  
print sqrt(5)
# 2.236
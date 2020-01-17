# Write a function that reverses the digits a 32-bit signed integer, x. Assume that the environment can only store integers within the 32-bit signed integer range, [-2^31, 2^31 - 1]. The function returns 0 when the reversed integer overflows.

""" Example:
Input: 123
Output: 321 """

class Solution:
    def reverse(self, x):
        answer = 0
        digits = 0
        sign = -1

        if x < 0:
            sign = -1
        else:
            sign = 1
        
        num = sign * x
        while num:
            digits += 1
            num = num // 10
        
        num = sign * x
        digits -= 1
        
        while num:
            answer = answer + pow(10,digits) * (num%10)
            num = num // 10
            digits -= 1
        
        if answer > pow(2,31)-1:
            return 0
        else:
            return sign * answer

print Solution().reverse(123)
# 321
print Solution().reverse(2**31)
# 0
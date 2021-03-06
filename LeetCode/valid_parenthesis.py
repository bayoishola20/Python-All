# VALID PARENTHESIS
class Solution:
    def isValid(self, s):
        paren = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        complete = []

        for i in s:                                                                 # loop through string
            if i in paren:                                                          # check if item is a parenthesis "key"
                complete.append(i)
            elif (len(complete) == 0 or paren[complete.pop()] != i ):               # if complete is empty or by checking each 
                return False 
        return True;
                
# Test 1
a = Solution()

# print(a.isValid(s = "()")) # True

# Test 2
# print(a.isValid(s = "()[]{}")) # True

# # Test 3
# print(a.isValid(s = "([)]")) # False

# # Test 4
# print(a.isValid(s = "(]")) # False

# # Test 5
print(a.isValid(s = "(())]")) # False
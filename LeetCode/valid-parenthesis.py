class Solution:
    def isValid(self, s: str) -> bool:
        paren = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        complete = []

        for i in s:             # loop keys of dict
            if i in paren:
                complete.append(i)
            elif (len(complete) == 0 or paren[complete.pop()] != i ):
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
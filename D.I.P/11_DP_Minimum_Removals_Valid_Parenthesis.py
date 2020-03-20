# You are given a string of parenthesis. Return the minimum number of 
# parenthesis that would need to be removed in order to make the string valid. 
# "Valid" means that each open parenthesis has a matching closed parenthesis.

def count_invalid_parenthesis(string):

    left_paren, right_paren = 0, 0              # store count of left and right parenthesis
    
    for i in string:                            # loop through the string input
        if i == '(':                            # check for left parenthesis and then increase count
            left_paren += 1
            # print "left_paren,", left_paren
        else:                                   # else i is ')'
            if left_paren > 0:                  # if left is greater than 0, then decrease count
                left_paren -= 1
                # print "left_paren,", left_paren
            else:
                right_paren += 1                # else increase count of right
                # print "right_paren,", right_paren
    return left_paren + right_paren             # return what is remaining of left and right.

    
print count_invalid_parenthesis("()())()")
# 1

print count_invalid_parenthesis("((()()()")
# 2
# Given an input string, reverse the string word by word.

def reverseWords(s):
    s = ''.join(s) # join string
    s = s.strip() # remove leading and trailing white spaces
    s = s.split(" ") # split along spaces
    ans = s[-1::-1] # reverses word in-place by taking last to first until first is last
    ans = ' '.join(ans) # join string by spaces
    output = ' '.join(ans.split()) # in case of double spaces, split by removing white space and then join again
    return output

print "\n"

first = "the sky is blue"
print "Input: " + first
print "Output: ", reverseWords(first)

print "\n"

second = "  hello world!  "
print "Input: " + second
print "Output: ", reverseWords(second)

print "\n"

third = "a good   example"
print "Input: " + third
print "Output: ", reverseWords(third)

print "\n"
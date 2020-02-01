# Given a list of words in a string, reverse the words in-place (ie don't create a new string and reverse the words). Since python strings are not mutable, you can assume the input will be a mutable sequence (like list).

def reverse_words(words):
  ans = ''.join(words) # join all characters in list to string
  ans = ans.split(" ") # split string by spaces
  ans = ans[-1::-1] # reverse in-place by taking last word to first until the very first is now the last
  output = ' '.join(ans) # join each word to string
  return output
  

s = list("can you read this")
print "INPUT:", ''.join(s)

print "OUTPUT: ", reverse_words(s)

# this read you can
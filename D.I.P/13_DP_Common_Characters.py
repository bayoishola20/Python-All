# Given a list of strings, find the list of characters that appear in all strings.

def common_characters(strs):
    unique = [ set(st) for st in strs ]                         # get list of unique characters for each string in list 
    common = unique[0].intersection(*unique[1:])                # using first string unique characters, find intersection with other strings unique characters
    return list(common)                                         # return. Set converted to list.
        


print common_characters(['google', 'facebook', 'youtube'])
# ['e', 'o']
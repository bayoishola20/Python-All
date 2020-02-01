'''
Given a string, returns the letters in uppercase as lowercase and vice-versa..

'''

def switch_case(string):
    result = '' # create an empty string
    for i in string: # loop through the string
        if i.islower(): # check if character is lower
            result += i.upper() # if lower, convert to upper, append to empty string and keep checking
        if i.isupper(): # check if character is upper
            result += i.lower() # if upper, convert to lower, append to empty string and keep checking
    return result

print switch_case("Arg")
# aRG
print switch_case("CrIcKeT")
# cRiCkEt

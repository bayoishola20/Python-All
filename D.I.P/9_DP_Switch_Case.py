'''
Given a string, returns the letters in uppercase as lowercase and vice-versa..

'''

def switch_case(string):
    result = ''
    for i in string:
        if i.islower():
            result += i.upper()
        if i.isupper():
            result += i.lower()
    return result

print switch_case("Arg")
# aRG
print switch_case("CrIcKeT")
# cRiCkEt

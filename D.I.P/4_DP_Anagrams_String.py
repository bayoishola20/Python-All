# Given 2 strings s and t, find and return all indexes in string s where t is an anagram.

def find_anagrams(s, t):
    # create and empty dictionary, get every unique character (i) as a key and its frequency as the value my_dict[i]
    my_dict = {}
    for i in t:
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1
    # print my_dict
    
    #reusable variables
    T = len(t)
    S = len(s)
    ans = []
    temp_dict = {}

    for j in range(S-T+1): # range + 1 to account for even number occurrence of anagram
        if not temp_dict:
            for k in s[j:j+T]: # check the main string
                if k not in temp_dict:
                    temp_dict[k] = 1
                else:
                    temp_dict[k] += 1
                    print temp_dict[k]
        else:
            temp_dict[ s[j-1] ] -= 1
            if s[j+T-1] in temp_dict:
                temp_dict[ s[j+T-1] ] += 1
            else:
                temp_dict[ s[j+T-1] ] = 1
            
        fit = True
        for n in my_dict.keys():
            if n not in temp_dict or my_dict[n] != temp_dict[n]:
                fit = False
                break
        if fit:
            ans += j,
    
    return ans


print find_anagrams('acdbacdacb', 'abc')
# [3, 7]
print find_anagrams('AAABABAAB', 'AABA')
# [0, 1, 4]
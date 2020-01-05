# Given 2 strings s and t, find and return all indexes in string s where t is an anagram.

def find_anagrams(s, t):

    my_dict = {}
    for i in t:
        if i in my_dict:
          my_dict[i] += 1
        else:
            my_dict[i] = 1
    
    T = len(t)
    S = len(s)
    ans, temp_dict = [], {}

    for j in range(S-T+1):
        if not temp_dict:
            for k in s[j:j+T]:
                if k not in temp_dict:
                    temp_dict[k] = 1
                else:
                    temp_dict[k] += 1
        else:
            temp_dict[s[j-1]] -= 1
            if s[j+T-1] in temp_dict:
                temp_dict[s[j+T-1]] += 1
            else:
                temp_dict[s[j+T-1]] = 1
            
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
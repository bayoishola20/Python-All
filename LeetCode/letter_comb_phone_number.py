''' Letter Combinations of a Phone Number
DIFFICULTY: MEDIUM
Given a string containing digits from 2-9 inclusive, return all possible letter
combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters. '''

import itertools

class Solution:
    def letterCombinations(self, digits: str):

        lookup = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        if len(digits) == 0: return [] 
        
        ans, soln = [], [""]

        tmp = [lookup[i] for i in digits]  # getting the letters equivalent for the digits

        for j in itertools.product(*tmp):  # product does the cartesian multiplication
            ans.append("".join(j))
        soln = ans

        return soln

a = Solution()

print(a.letterCombinations("23")) # ["ad","ae","af","bd","be","bf","cd","ce","cf"]

# print(a.letterCombinations("249")) # ['agw', 'bgw', 'cgw', 'ahw', 'bhw', 'chw', 'aiw', 'biw', 'ciw', 'agx', 'bgx', 'cgx', 'ahx', 'bhx', 'chx', 'aix', 'bix', 'cix', 'agy', 'bgy', 'cgy', 'ahy', 'bhy', 'chy', 'aiy', 'biy', 'ciy', 'agz', 'bgz', 'cgz', 'ahz', 'bhz', 'chz', 'aiz', 'biz', 'ciz']

# print(a.letterCombinations("")) # []

# print(a.letterCombinations("2")) # ["a","b","c"]
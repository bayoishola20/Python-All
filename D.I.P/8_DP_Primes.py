""" 
Given a positive integer n, find all primes less than n.
"""


def find_primes(n):

    # initialize empty array to store primes
    result = []
    for i in range(2, n): # loop through starting from 2 which is the smallest prime number to n
        isPrime = True # a truthy for prime numbers
        for j in range(2, i): # loop through starting from 2 to i: So, from loop from 2 to 2, from 2 to 3, then from 2 to 4
            if i % j == 0: # check if each number divided by each has a remainder of zero(0).
                isPrime = False # then isPrime is False
        if isPrime: # all other values, that is, that isPrime
            result.append(i) # append to empty list
    return result #return result

    # list comprehension alternative
    # return [x for x in range(2, n) if all(x % y != 0 for y in range(2, x))]


print find_primes(14)
# [2, 3, 5, 7, 11, 13]
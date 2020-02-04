##### Topic 1: Working with standard Python lists

''' Create a random list

Create a nested list of 60 elements arranged in 10 sub-lists of 6 entries each to be filled with randomly distributed integer values between 0 and 15 '''

import random

# using list comprehension

print "Nested list (list comprehension): ", [[random.randrange(0,15) for _ in range(10)] for _ in range(6)]

print "\n"

# using explicit for loops
outer = []
for _ in range(6):
  inner = []
  for _ in range(10):
    inner.append( random.randrange(0,15) )
  outer.append(inner)

print "Nested list (for loop): ", outer

print "\n"

''' Produce a histogram from the values

Then, propagate through the list of 60 integer elements and count how often each value exists within the nested list. 
A dictionary of the type {value : frequency, value : frequency, value :
 frequency} will be an ideal structure to take up the results.
'''

flatten = []

for inner in outer:
  for i in inner:
    flatten.append(i)

print "Flattened: ", flatten

print "\n"


my_counter = {} # empty dictionary to store value: frequency

# first flatten list
for inner in outer:
  for i in inner:
    # my_counter.get(index, value). Value is optional. Returns the value of the item with the specified key 
    # my_counter[i] = ... sets value associated with key i.
    # Putting 0 so it returns integer and plus 1 to continue else would give all zeros.
    my_counter[i] = my_counter.get(i, 0) + 1

print "Frequency: ", my_counter

print "\n"

''' Display the histogram

Produce a simple but well-formatted screen output to display the histogram.
It will be up to you to use a tabular form (formatted print) or, with a
higher effort, in a graphic form. The latter will require to have a look into
the package "Matplotlib" which provides a nearly unlimited number of
graphic options. For the option of formatted print, a clever shortcut is to
cast the integer values with the python repr()-Operator for easy
justification. '''

print "{:<8} {:<8}".format('Value', 'Frequency')

for key, val in my_counter.items():
  frequency = val # not so necessary line of code
  print "{:<8} {:<8}".format(key, val)

print "\n"



''' Outlook
We can get the same data and structures in an even more efficient way by
storing the nested list as a NumPy array (but this is a topic for a later
session). '''

import numpy as np
# 0, 15 is the range
# size of 2D array as a tuple (6,10) [Could be an int] and casting to type int
print np.random.randint(0, 15, (6,10)).astype(int)

print "\n"

print np.random.randint(0,15,(6,10)).astype(int)

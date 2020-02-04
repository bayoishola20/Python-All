# Topic 0: Elementary operations using standard Python lists

# 1. Create random lists

import random

a = []
for _ in range(0, 20):
  a.append(random.randrange(0,20))

print "a: ", a

print "\n"


b = []

for _ in range(0,20):
  b.append(random.randrange(0,20))

print "b: ", b

print "\n"


# 2. Derive some basic descriptors for each list

print "Length list operator: ", len(a), len(b)

print "\n"

print "Maximum list operator: ", max(a), max(b)

print "\n"

print "Minimum list operator: ", min(a), min(b)

print "\n"


# 3. Fuse the two lists
fused = a + b

print "fused list: ", fused

print "\n"

# 4. Modify the fused list and derive further descriptors

print "sorted list (ascending): ", sorted(fused, reverse=False)

print "\n"

print "sorted reversed list (descending): ", sorted(fused, reverse=True)

print "\n"

# reversed needs to be wrapped in a list() else it returns a listreverseiterator object
print "Reversed: ", list( reversed(fused) )

print "\n"

#  list of unique elements (all occurrences shall only be listed once)

print "Unique elements: ", set(fused)

print "\n"

# create a list which shows the ranks of each list element (defined in ascending order) of the original unsorted fused list

def rankArray(arr): 
      
    # create vector of 0's to hold ranks 
    rank_arr = []
    for _ in range( len(arr) ):
      rank_arr.append(0)

  
    # create auxilliary array to store array of tuples for each integer input in the array along with their indices 
    aux_arr = []
    for index, x in enumerate( range( len(arr) ) ):
      aux_arr.append( (arr[index], x) ) 

  
     # sort using key. lambda function is used to get key values
     # this produces an array of tuples with their rank as the first item and the value itself as the second

     # lambda arguments : expression 
  
    # Sort aux_arr according to first element 
    aux_arr.sort(key=lambda x: x[0])

    i = 0
    n = 1
    rank = 1
  
    while i < len(arr): 
        j = i 
  
        # get elements with same rank 
        while j < len(arr) - 1 and aux_arr[j][0] == aux_arr[j + 1][0]: 
            j += 1
        n = j - i + 1
  
        for j in range(n): 
            # for each equal value, obtain
            # index aux_arr[i+j][0] in arr 
            idx = aux_arr[i+j][1] 
            rank_arr[idx] = rank + (n - 1) * 0.5
  
        # increment rank and i 
        rank += n 
        i += n 
  
    return rank_arr

print "Ranked array: ", rankArray( fused )
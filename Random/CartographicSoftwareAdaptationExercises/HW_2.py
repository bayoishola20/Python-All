# Topic 2: Analyse List Elements for Common Members

'''
Create a nested list of positive integer values spanning the range between 1
and 10. Create 10 groups of 4 members each.
'''
import random

outer = []

for _ in range(10):
  inner = []
  for _ in range(4):
    inner.append(random.randint(1,10))
  outer.append(inner)

print "Array (for loop approach) is: ", outer

# list comprehension approach

print "Array (list comprehension approach) is: ", [[random.randint(1,10) for _ in range(4)] for _ in range(10)]
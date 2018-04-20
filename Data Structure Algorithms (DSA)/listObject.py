a = [1, 2, 3, 4]

for i in xrange(len(a)):
    print a[i]

# del a[0]
try:
    print a.index(5)
except:
    print "element unavailable"

print sorted(a)
a.sort()
print a

# List Comprehension

#===== These two sets of code are same===#

def f(x):
    return x**2
print f(5)

print [f(x) for x in xrange(10)]

#=========================================#

class sample:
    def __init__(self):
        self.value = 10

for _ in xrange(10):
    new_sample = sample()
    print new_sample
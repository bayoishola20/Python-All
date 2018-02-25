a, b = 0, 1
for x in xrange(0, 10):
    print a
    a, b = b, a + b

#fibonacci generator
def fib(num):
    a, b = 0,1
    for x in xrange(num):
        yield "{}: {}".format(x+1, a)
        a, b = b, a + b

for items in fib(10):
    print items
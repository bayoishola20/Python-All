# check if odd or even

data = [1,2,4,5,6,7,10]

for i in data:
    if i % 2 == 0:
        print i, " is even"
    else:
        print i, " is odd"

print "\n"

aDict = {"first": 22,
         "second": "twenty-two",
         "third": "XXII"} # dictionary is unordered

for k in aDict:
    print k, aDict[k]



print "\n"

print 0b10 # binary, base 2

print "\n"

print 0o10 # Octadecimal, base 8

print "\n"

print 0x10 # Hexadecimal, base 16

print "\n"

print .4e7
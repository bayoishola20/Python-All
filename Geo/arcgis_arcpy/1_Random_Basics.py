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
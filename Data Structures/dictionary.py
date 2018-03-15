# Performance benchmark
import random
import time

animals = ["dog", "cat", "pigeon", "chimpanzee", "elephant", "lion"]

def create_dataset():
    num_inputs = 100000
    f = open('data1.txt', "w")
    for i in xrange(num_inputs):
        current = random.choice(animals)
        f.write(current + "\n")
    f.close()

def read_list(): # function reads dataset list
    count = []
    for j in animals:
        count.append(0)
    with open("data1.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line != "": # checks if not last line in file
                count[animals.index(line)] += 1
    print count

def read_dict(): # function reads dataset dictionary
    count = {}
    for k in animals:
        count[k] = 0
    with open("data1.txt") as f:
        for line in f:
            line = line.strip()
            if line != "":
                count[line] += 1
    print count

t0 = time.time()
create_dataset()
t1 = time.time()
print "Creation of dataset took %0.1f seconds\n" % (t1-t0)

t0 = time.time()
read_list()
t1 = time.time()
print "List took %0.1f seconds\n" % (t1-t0)

t0 = time.time()
read_dict()
t1 = time.time()
print "Dictionary took %0.1f seconds\n" % (t1-t0)
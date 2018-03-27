import random

def generate_file():
    f = open("data3.txt", "w")
    for i in xrange(50):
        f.write(str(random.randint(0, 50)) + "\n")
    f.close()

def selection_sort(my_list):
    sorted_list = 0 # length of sorted list
    while sorted_list < len(my_list):
        minimum_index = None # index of largest item
        for j, k in enumerate(my_list[sorted_list:]):
            if minimum_index == None or k < my_list[minimum_index]:
                minimum_index = j + sorted_list
        # swap arrangement
        my_list[sorted_list], my_list[minimum_index] = my_list[minimum_index], my_list[sorted_list]
        sorted_list += 1
    return my_list     

# add bubble sort to compare

def bubble_sort(my_list):
    swapped = True
    while swapped:
        swapped = False
        for i in xrange(1, len(my_list)):
            if my_list[i-1] > my_list[i]:
                my_list[i], my_list[i-1] = my_list[i-1], my_list[i]
                swapped = True
    return my_list

# add builtin sort to compare



generate_file()

my_list = [int(data) for data in open("data3.txt", "r").readlines()]

print my_list
print "Length of unsorted data: ", len(my_list)
print selection_sort(my_list)
print "Length of sorted data: ", len(selection_sort(my_list))

selection_time = []
bubble_time = []
builtin_time = []

from time import time

n = [1, 10, 100, 1000, 10000]
for benchmark in n:
    t0 = time()
    s = sorted(my_list)
    t1 = time()
    builtin_time.append(t1-t0)

    t0 = time()
    s = selection_sort(my_list)
    t1 = time()
    selection_time.append(t1-t0)

    t0 = time()
    s = bubble_sort(my_list)
    t1 = time()
    bubble_time.append(t1-t0)

print "n \t Builtin \t Selection  \t Bubble", "\n", "=================================================="

for x, y in enumerate(n):
    print "%d \t %0.5f \t %0.5f \t %0.5f" % (y, builtin_time[x], selection_time[x], bubble_time[x])
import random

def generate_file():
    f = open("data4.txt", "w")
    for i in xrange(50):
        f.write(str(random.randint(0, 50)) + "\n")
    f.close()

def bubble_sort(my_list):
    swapped = True
    while swapped:
        swapped = False
        for i in xrange(1, len(my_list)):
            if my_list[i-1] > my_list[i]:
                my_list[i], my_list[i-1] = my_list[i-1], my_list[i]
                swapped = True
    return my_list

generate_file()

my_list = [int(data) for data in open("data4.txt", "r").readlines()]

print my_list
print "Length of unsorted data: ", len(my_list)
print bubble_sort(my_list)
print "Length of sorted data: ", len(bubble_sort(my_list))
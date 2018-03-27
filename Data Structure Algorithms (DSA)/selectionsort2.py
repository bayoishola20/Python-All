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

generate_file()

my_list = [int(data) for data in open("data3.txt", "r").readlines()]

print my_list
print "Length of unsorted data: ", len(my_list)
print selection_sort(my_list)
print "Length of sorted data: ", len(selection_sort(my_list))
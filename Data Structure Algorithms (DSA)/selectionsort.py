'''Selection sort is a simple sorting algorithm. This sorting algorithm is an in-place comparison-based algorithm in which the list is divided into two parts, the sorted part at the left end and the unsorted part at the right end. Initially, the sorted part is empty and the unsorted part is the entire list.

The smallest element is selected from the unsorted array and swapped with the leftmost element, and that element becomes a part of the sorted array. This process continues moving unsorted array boundary by one element to the right.'''


import random

def generate_file():
    f = open("data2.txt", "w")
    for i in xrange(0, 1000):
        f.write(str(random.randrange(1, 100000)) + "\n")
    f.close()

def arrange(nums, first, second):
    ans = nums[first]
    nums[first] = nums[second]
    nums[second] = ans

def selection_sort(input_list):
    for j in xrange(len(input_list)):
        maximum_index = j

        for k in xrange(j+1, len(input_list)):
            if input_list[k] > input_list[maximum_index]:
                maximum_index = k
        
        arrange(input_list, maximum_index, j)

    return input_list

generate_file()

my_list = [int(data) for data in open("data2.txt", "r").readlines()]

sorted_data = selection_sort(my_list)

print "Length of sorted data: ", len(sorted_data), "\n", [str(n) + " " for n in sorted_data[:100]]
# Now let us create a function that accepts parameters and transforms them as needed. This
# function will accept a number and multiply it by 3

def three_multiple(num):
    return "multiple of %i is %i" % (num, num*3)
print three_multiple(5)
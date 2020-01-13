# Now let us create a function that accepts parameters and transforms them as needed. This
# function will accept a number and multiply it by 3

def three_multiple(num):
    return "multiple of %i is %i" % (num, num*3)
print three_multiple(5)

print "\n"

# Funtion above doesn't check for data type of input and could throw an exception


# this function validates data type of int and return no value if not int number
def three_multiple_con(num):
    if type(num) == type(1) or type(num) == type(1.0):
        return "CONDITION: multiple of %i is %d" %(num, num*3)

print three_multiple_con(4)

print "\n"


# similar function above but with a default parameter and the other takes an input

def three_multiple_param(num, multiplier = 3):
    if type(num) == type(1) or type(num) == type(1.0):
        return "PARAMETER: multiple of %i with multiplier %i is %i" %(num, multiplier, num*multiplier)

print three_multiple_param(7, 4)
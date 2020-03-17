# Given an integer, reverse the digits. Do not convert the integer into a string and reverse it.

def reverse_integer(num):
    reverse = 0                                         # fully reversed integer

    sign = -1 if num < 0 else 1                         # check for integer sign


    digits = 0                                          # stores total digits count of integers
    
    x = sign * num                                      # enforces positive integers

    while x:                                            # truth statment for the given integer
        digits += 1                                     # stores digits counts
        x = x // 10                                     # gets last digits - floor division that rounds down to nearest whole number
    

    x = sign * num

    digits -= 1                                         # reduces digits count by 1
    

    while x:
        reverse = reverse + pow(10,digits) * (x%10)     # pow(10,digits) gives Hundreds Tens Units of integer and then multiplies by remainder

        x = x // 10                                     # floor division rounded down to nearest whole number
        digits -= 1
    


    if reverse > pow(2,31)-1:                        # returns False
        return 0
    else:                                            # else return with sign
        return sign * reverse
  
print reverse_integer(135)
# 531

print(reverse_integer(342))
# 243

print reverse_integer(-321)
# -123
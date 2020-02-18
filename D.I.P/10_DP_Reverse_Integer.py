# Given an integer, reverse the digits. Do not convert the integer into a string and reverse it.

def reverse_integer(num):
    reverse = 0

    while (num > 0):
        lastDigit = num % 10 # modulo gets last digit which is the the remainder when you divide by 10
        reverse = (reverse * 10) + lastDigit # concatenate last digit to reverse: this brings last digit to "Tens" by adding a zero
        num = num // 10 # remove last digit from number
    return reverse
    """ answer = 0
    digits = 0
    sign = -1 if x < 0 else 1
    
    num = sign * x
    while num:
        digits += 1
        num = num // 10
    
    num = sign * x
    digits -= 1
    
    while num:
        answer = answer + pow(10,digits) * (num%10)
        num = num // 10
        digits -= 1
    
    if answer > pow(2,31)-1:
        return 0
    else:
        return sign * answer """
  
print reverse_integer(135)
# 531

print(reverse_integer(342))
# 243

print reverse_integer(-321)
# -123
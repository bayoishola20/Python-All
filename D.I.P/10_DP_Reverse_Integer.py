# Given an integer, reverse the digits. Do not convert the integer into a string and reverse it.

def reverse_integer(num):
    reverse = 0

    while (num > 0):
        lastDigit = num % 10 # modulo gets last digit which is the the remainder when you divide by 10
        reverse = (reverse * 10) + lastDigit # concatenate last digit to reverse: this brings last digit to "Tens" by adding a zero
        num = num // 10 # remove last digit from number
    return reverse
  
print reverse_integer(135)
# 531

print(reverse_integer(342))
# 243

print reverse_integer(-321)
# -123
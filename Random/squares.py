items = map(int, raw_input("Enter comma seperated integers: ").split(","))

#using list comprehensions
squares = [num*num for num in items]
print squares
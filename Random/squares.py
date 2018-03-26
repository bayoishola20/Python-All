items = map(int, raw_input().split())

#using list comprehensions
squares = [num*num for num in items]
print squares
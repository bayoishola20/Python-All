#simple calculator script
while True:
  print "Select:"
  print "Enter 'Add' for addition"
  print "Enter 'Minus' for subtraction"
  print "Enter 'Multiply' for multiplication"
  print "Enter 'Divide' for division"
  print "Enter 'Square' for finding squares"
  print "Enter 'Cube' for finding cubes"
  print "Enter 'Square root' for square roots"
  print "Enter 'Percentage' for percentage of a number"
  print "Enter 'Multiples' for multiples of a number from 1 to 12"
  print "Enter 'End' to quit/terminate calculator"
  user_input = raw_input(">>")
  
  if user_input == "End":
    break
  elif user_input == "Add":
    num1 = float(raw_input("First number:"))
    num2 = float(raw_input("Second number:"))
    answer = str(num1 + num2)
    print answer
  elif user_input == "Minus":
    num1 = float(raw_input("First number:"))
    num2 = float(raw_input("Second number:"))
    answer = str(num1 - num2)
    print answer
  elif user_input == "Multiply":
    num1 = float(raw_input("First number:"))
    num2 = float(raw_input("Second number:"))
    answer = str(num1 * num2)
    print answer
  elif user_input == "Divide":
    num1 = float(raw_input("First number:"))
    num2 = float(raw_input("Second number:"))
    answer = str(num1 / num2)
    print answer
  elif user_input == "Square":
    num = float(raw_input("Enter number:"))
    answer = str(num ** 2)
    print answer
  elif user_input == "Cube":
    num = float(raw_input("Enter number:"))
    answer = str(num ** 3)
    print answer
  elif user_input == "Square root":
    num = float(raw_input("Enter number:"))
    answer = str(num ** 0.5)
    print answer
  elif user_input == "Percentage":
    num = float(raw_input("Enter number:"))
    answer = str(num / 100) + "%"
    print answer
  elif user_input == "Multiples":
    num = float(raw_input("Enter number:"))
    if num > 0:
      for i in range(1,13):
        print num * i
    else:
      print "Something is wrong!"
  else:
    print "Invalid. Try again"
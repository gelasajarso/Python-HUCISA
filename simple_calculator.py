# Python script that takes two numbers and an operator (+, -, *, /) as input and prints the result.
first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
operator = input("Select operator: ")

if(operator == "+"):
  print("Sum: ", first_number+second_number)
elif(operator == "-"):
  print("Difference: ", first_number-second_number)
elif(operator == "*"):
  print("Product: ", first_number*second_number)
elif(operator == "/"):
  print("Quotient: ", first_number/second_number)
else:
  print("please enter the correct operator")

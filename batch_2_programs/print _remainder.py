#input two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

#set rules and coditions
if num2 != 0:
    remainder = num1 % num2
    print("remainder is: ", remainder)
    #print output
else:
    print("Division by zero is not allowed")
#deny division by zero

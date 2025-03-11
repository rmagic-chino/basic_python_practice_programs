#input two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

#set rules
if num2 != 0:
    quotient = int(num1 // num2)
    print("The quotient is", quotient)
   #disable deciamls
#output division
else:
    print("Division by zero is not allowed")
   #deny division by zero

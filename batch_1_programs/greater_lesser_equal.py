#input two numbers
#give conditions to find out which number is greater, lesser or equal
#output the result

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print(num1, "is greater than", num2)
elif num1 < num2:
    print(num1, "is lesser than", num2)
else:
    print(num1, "is equal to", num2)
#output
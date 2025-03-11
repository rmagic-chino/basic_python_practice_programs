#initialize empty list
numbers = []

#input 10 numbers
for number in range(10):
    number = int(input("Enter a number: "))
    numbers.append(number)

#set conditions
total = sum(numbers)
#print result
print("The sum is:", total)
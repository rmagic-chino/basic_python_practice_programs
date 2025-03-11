#initialize
numbers = []

#input 10 numbers
for number in range(10):
    num = float(input("Enter a number: "))
    numbers.append(num)

#set rules and coditions
result = numbers[0]

#subtract 10 from each number
for num in numbers[1:]:
    result -= num
#output
print(result)
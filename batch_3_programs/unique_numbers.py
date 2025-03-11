#initialize
values = []

#initialize for loop
for number in range(10):
    num = float(input("Enter a number: "))
    values.append(num)
#input 10 numbers

#initiaize a list to store the unique numbers
unique = []

#initialize a for loop to iterate through the list of numbers
for num in values:
    if values.count(num) == 1:
        unique.append(num)

#print the unique numbers
print("Unique numbers: ", unique)

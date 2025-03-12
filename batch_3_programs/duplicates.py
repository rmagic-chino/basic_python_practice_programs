#initialize
values = []
unique = []

#initialize rules and condiitons
for number in range(10):
    num = float(input("Enter a number: "))
    if num not in unique:
        unique.append(num)
    values.append(num)

#print output
print("Unique numbers: ", unique)

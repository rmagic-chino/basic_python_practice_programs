#initialize
count = 0

#display message enter 10 numbers
print("Enter 10 numbers:")
for number in range(10):
    num = int(input())
    if num % 2 != 0:
        print(num)
        count += 1
#put conditions and display only odd numbers
     #put rules for odd numbers

print("Number of odd numbers:", count)
#print the odd numbers
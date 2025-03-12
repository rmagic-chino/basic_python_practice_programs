#initialize
numbers = []

#while loop
    #input number
while True:
    try:
        num = float(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        break
    #set rules for the loop

#initialize
numbers.sort()
print("numbers in order:", numbers)
#print nums from low to high

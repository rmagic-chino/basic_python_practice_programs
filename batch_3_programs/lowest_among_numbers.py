#initialize
lowest = None

#while loop
    #set rules for the loop
while True:
    try:
        num = float(input("Enter a number: "))
        if lowest is None or num < lowest:
            lowest = num
    except ValueError:
        break

print("The lowest number is", lowest) #
#print the lowest number

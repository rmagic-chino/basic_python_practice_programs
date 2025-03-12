#initialize
values = []

#while loop enter as many numbers
while True:
    try:
        num = float(input("Enter a number: "))
        if num in values:
            print("Duplicate")
   #put rules and conditions
        else:
            values.append(num)
            print("Unique")
   #determine if uniqie or duplicate
    except ValueError:
        print("Invalid input")
        break
    #print output
    
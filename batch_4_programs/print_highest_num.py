#initialize
def highest_number():
    numbers = []

    #set while loop
    while True:
        try:
            numbers.append(int(input("enter a number: ")))
        except ValueError:
            break
#print output
    print("Highest number:", max(numbers) if numbers else "No numbers entered.")

#execute 
highest_number()

#define commands
def average_number():
    numbers = []

    #construct while loop
    while True:
        try:
            numbers.append(int(input("enter a number: ")))
        except ValueError:
            break

    #set rules and conditions
    if numbers:
        avg = sum(numbers) / len(numbers)
        print("average of numbers:")
        print(avg)
    else:
        print("no numbers entered.")

#execute
average_number()

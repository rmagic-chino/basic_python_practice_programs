#define commands
def sort_numbers():
    numbers = []

    #construct while loop
    while True:
        try:
            numbers.append(int(input("enter a number")))
        except ValueError:
            break    

#set rules and conditions
    if numbers:
        print("numbers from highest to lowest:")
        print(sorted(numbers, reverse=True))
    else:
        print("no numbers entered")

#execute
sort_numbers()

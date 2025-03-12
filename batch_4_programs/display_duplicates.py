#define command
def find_duplicates():
    numbers = [int(input("enter a number: ")) for i in range(10)]
    duplicates = {num for num in numbers if numbers.count(num) > 1}

    print("The duplicates are: ", duplicates)
    #print duplicate numbers

find_duplicates()
#execute command

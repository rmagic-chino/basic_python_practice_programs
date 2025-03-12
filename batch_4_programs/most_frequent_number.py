#import counter
from collections import Counter

#define a function that takes a list of numbers as input
def most_frequent_number():
    numbers =[]

    while True:
        try:
            numbers.append(int(input("enter a number")))
        except ValueError:
            break

    #construct while loop
    if numbers:
        max_count = max(Counter(numbers).values())
        most_common = [num for num, count in Counter(numbers).items() if count == max_count]
        print("Most frequent number(s):", most_common)
    else:
        print("No numbers entered.")

most_frequent_number()
#execute command

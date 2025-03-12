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

#set rules and conditions
#execute command
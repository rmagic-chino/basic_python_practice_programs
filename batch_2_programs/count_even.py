#initalize
even_count = 0

#set rules and conditions
for number in range(10):
    num = int(input("Enter a number: "))
    if number % 2 == 0:
        even_count += 1
#set variables

print("The number of even numbers is: ", even_count)
#print output

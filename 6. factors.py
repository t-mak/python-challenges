number = int(input("Enter a positive integer: "))

for number_value in range(1, number+1):
    if number % number_value == 0:
        print (f"{number_value} is a factor of {number}")

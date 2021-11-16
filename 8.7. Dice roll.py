"""Write a function called roll() that uses the randint() function to
simulate rolling a fair die by returning a random integer between
1 and 6 ."""

import random

def roll():
    return random.randint(1,6)

sum_of_rolls = 0
num_of_rolls = 100

for trial in range(num_of_rolls):
    roll_value = roll()
    sum_of_rolls = sum_of_rolls + roll_value
    print("Rolled: ", roll_value)

avg_of_rolls = sum_of_rolls / num_of_rolls
print(f"Average roll is: {avg_of_rolls:.0f}")



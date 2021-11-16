import random

def flip_coin():
    if random.randint(0, 1) == 0:
        return "heads"
    else:
        return "tails"

sum_of_flips = 0
num_of_series = 10_000

for trial in range(num_of_series):
    heads = False
    tails = False
    while 1:  
        if flip_coin() == "heads":
            heads = True
            # print("Flipped heads")
        else:
            tails = True
            # print("Flipped tails")
        sum_of_flips = sum_of_flips + 1
        # print(f"Sum of flips for series {trial} is currently {sum_of_flips}")
        if heads and tails:
            break

print(f"The average number of coin flips needed to contain both heads and tails for {num_of_series} of series is {sum_of_flips / num_of_series}")

"""Need to flip coins till I get both heads and tails
Count times how many it took to have both tails and heads
Then count average of flips needed in 10000 such series to get both heads and tails"""

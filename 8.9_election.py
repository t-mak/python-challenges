import random

num_of_votings = 10_000
region_1_chance = 0.87
region_2_chance = 0.65
region_3_chance = 0.17

#region1_wins = 0
#region2_wins = 0
#region3_wins = 0

wins = 0

def region_vote(region_win_chance):
    if random.random() < region_win_chance:
        return 1
        # won
    else:
        return 0
        # lost

for trial in range(num_of_votings):
    if region_vote(region_1_chance) + region_vote(region_2_chance) + region_vote(region_3_chance) >= 2:
        wins = wins + 1

"""
    region1_result = 0
    region2_result = 0
    region3_result = 0
    
    region1_result = region_vote(region_1_chance)
    region2_result = region_vote(region_2_chance)
    region3_result = region_vote(region_3_chance)

    region1_wins = region1_wins + region1_result
    region2_wins = region2_wins + region2_result
    region3_wins = region3_wins + region3_result

    if region1_result + region2_result + region3_result >= 2:
        wins = wins + 1
"""

print(f"Win percentage chance for Candidate A is {wins/num_of_votings:.0%}")

#print(f"Win percentage chance for Candidate A in region 1 is {region1_wins/num_of_votings}")
#print(f"Win percentage chance for Candidate A in region 2 is {region2_wins/num_of_votings}")
#print(f"Win percentage chance for Candidate A in region 3 is {region3_wins/num_of_votings}")

""" 2 candidates
3 voting regions
simulate election 10000 times and print percentage of candidate A wins
candidate wins an election if they win at least in 2 regions

Chances for winning for candidate A:
region 1 - 87%
region 2 - 65%
region 3 - 17%

Print percentage where candidate A wins
"""

import sys
import math
import itertools

# Get the first command-line argument (# spades, clubs, diamonds, hearts)
figgie_hand = sys.argv[1:]

spades, clubs, diamonds, hearts = list(figgie_hand)
print(f"{spades} spades")
print(f"{clubs} clubs")
print(f"{diamonds} diamonds")
print(f"{hearts} hearts")


suits_array = [int(x) for x in list(figgie_hand)]

# keeps track of the combinations where the given suit has 12 cards
suit_combs = [0, 0, 0, 0]
possible_combs = list(set(list(itertools.permutations([12,10,10,8]))))
for combo in possible_combs:
    twelve = combo.index(12)
    goal_suit = (5 - twelve) % 4
    suit_combs[goal_suit] += math.comb(combo[0], suits_array[0]) * math.comb(combo[1], suits_array[1]) * math.comb(combo[2], suits_array[2]) * math.comb(combo[3], suits_array[3])

total_comb = sum(suit_combs)
print("--------------")
print("Probability of being the goal suit:")
print(f"Spades: {round(suit_combs[0]/total_comb * 100, 1)}%")
print(f"Clubs: {round(suit_combs[1]/total_comb * 100, 1)}%")
print(f"Diamonds: {round(suit_combs[2]/total_comb * 100, 1)}%")
print(f"Hearts: {round(suit_combs[3]/total_comb * 100, 1)}%")

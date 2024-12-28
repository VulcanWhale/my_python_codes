#Python program to shuffle a deck of cards
import random

# taking the cards
ranks = range(1,14)
suits = ['Spade','Heart','Diamond','Club']

#making the deck of cards
deck = [(r,s) for r in ranks for s in suits]

# using random module to shuffle the cards
random.shuffle(deck)

# no we need to print the first five cards from the shuffled deck

print("The cards you got are as follows: ")
for i in range(5):
    print(f"{deck[i][0]} of {deck[i][1]}")

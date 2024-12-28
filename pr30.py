#Python program to shuffle a deck of cards
import random

# taking the cards
ranks = range(1,14)
suits = ['Spade','Heart','Diamond','Club']

#making the deck of cards
deck = [(r,s) for r in ranks for s in suits]

random.shuffle(deck)
import random

cards = input()
shuffles = int(input())
deck_of_cards = cards.split(" ")

for shuffle in range(1, int(len(deck_of_cards)/2)):
    random.shuffle(deck_of_cards[1::-2])

print(deck_of_cards)

deck_of_cards = input().split()
shuffles = int(input())

for shuffle in range(shuffles):
    shuffled_deck = []
    shuffled_deck_first_side = []
    shuffled_deck_second_side = []
    deck_middle = int(len(deck_of_cards) / 2)

    for first_side in range(deck_middle):
        shuffled_deck_first_side.append((deck_of_cards[first_side]))

    for second_side in range(deck_middle, len(deck_of_cards)):
        shuffled_deck_second_side.append(deck_of_cards[second_side])

    for shuffles in range(len(shuffled_deck_second_side)):
        shuffled_deck.append(shuffled_deck_first_side[shuffles])
        shuffled_deck.append(shuffled_deck_second_side[shuffles])

    deck_of_cards = shuffled_deck
    shuffled_deck_first_side.clear()
    shuffled_deck_second_side.clear()

print(shuffled_deck)

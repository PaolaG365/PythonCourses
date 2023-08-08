import random
'''
A classic game of rock, paper, scissors.
'''

rock_paper_scissors = {
    'rock': [
        {'result': 'You win!', 'computer move': 'scissors'},
        {'result': 'You lose!', 'computer move': 'paper'},
        {'result': 'Draw!', 'computer move': 'rock'}
    ],
    'paper': [
        {'result': 'You win!', 'computer move': 'rock'},
        {'result': 'You lose!', 'computer move': 'scissors'},
        {'result': 'Draw!', 'computer move': 'paper'}
    ],
    'scissors': [
        {'result': 'You win!', 'computer move': 'paper'},
        {'result': 'You lose!', 'computer move': 'rock'},
        {'result': 'Draw!', 'computer move': 'scissors'}
    ]
}
moves_dict = {"r": "rock", "p": "paper", "s": "scissors"}
moves = "rps"
print("This is a rock, paper, scissors game and you're playing against the pc."
      "\nEnter your choice by typing s for scissors, p for paper or r for rock."
      "\nYou can type 'exit' to quit at any time.")


def rps_game():

    player_move = input("Choose [r]ock, [p]aper or [s]cissors: ")
    computer_move = random.choice(moves)

    if player_move.lower() == 'exit':
        print("Exiting the game...")
        exit()

    if player_move not in moves:
        print("Invalid input! Try again...")
        return rps_game()

    player_move = moves_dict[player_move]
    computer_move = moves_dict[computer_move]
    print(f"The computer chose: {computer_move}.")

    for result in rock_paper_scissors[player_move]:
        if computer_move == result['computer move']:
            print(result['result'])

    return rps_game()


rps_game()

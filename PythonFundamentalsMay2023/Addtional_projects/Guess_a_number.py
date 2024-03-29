import random
'''
Guess a random number generated by the computer.
'''
print("Guess what random number between 1 and 100 the computer has generated.")
print("You can type exit at any time to quit.")


def exiting_game():
    print("Exiting the program! Bye!!!")
    exit()


def guess_a_number():
    chosen_number = random.randint(1, 100)

    while True:
        user_guess = input("Guess the number: ")

        if user_guess.lower() == "exit":
            exiting_game()

        if not user_guess.isdigit():
            print("Invalid input! Try again...")
            return guess_a_number()

        user_guess = int(user_guess)

        if user_guess > chosen_number:
            print("Too high!")
        elif user_guess < chosen_number:
            print("Too low!")
        else:
            print("You guessed it correctly! Nice job!")
            player_choice = input("Would you like to try again? Type Y for yes or N for no: ")
            if player_choice.lower() == "y":
                return guess_a_number()
            elif player_choice.lower() == "n":
                exiting_game()


guess_a_number()

def memory_game(game_board, user_moves, user_command):
    if not game_board or (not game_board and user_command == "end"):  # win
        print(f"You have won in {user_moves} turns!")
        return

    if user_command == "end" and game_board:  # game over
        print(f"Sorry you lose :(")
        print(*game_board)
        return

    user_moves += 1
    user_command = user_command.split()
    first_index, second_index = int(user_command[0]), int(user_command[1])

    # checks valid input
    if first_index == second_index or len(game_board) - 1 < first_index or first_index < 0\
            or len(game_board) - 1 < second_index or second_index < 0:
        middle_of_board = len(game_board) // 2
        game_board.insert(middle_of_board, f"-{user_moves}a")
        game_board.insert(middle_of_board + 1, f"-{user_moves}a")
        print("Invalid input! Adding additional elements to the board")

    # check if board elements are the same and removes them
    elif game_board[first_index] == game_board[second_index]:
        print(f"Congrats! You have found matching elements - {game_board[first_index]}!")
        number = game_board[first_index]
        game_board.remove(number)
        game_board.remove(number)

    # if they are not prompts user to try again
    elif game_board[first_index] != game_board[second_index]:
        print("Try again!")

    user_command = input()

    # saves current game stats and calls function again
    return game_board, user_moves, user_command, memory_game(game_board, user_moves, user_command)


numbers_board = input().split()
moves = 0
command = input()
memory_game(numbers_board, moves, command)

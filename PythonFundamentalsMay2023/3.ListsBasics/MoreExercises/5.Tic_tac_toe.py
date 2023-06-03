first_line = input().split()
second_line = input().split()
third_line = input().split()

first_line = [int(x) for x in first_line]
second_line = [int(x1) for x1 in second_line]
third_line = [int(x2) for x2 in third_line]

game = [first_line] + [second_line] + [third_line]

FIRST_PLAYER_WINNER = False
SECOND_PLAYER_WINNER = False

for line in range(len(game)):

    if len(set(game[line])) == 1:
        if game[line][line] == 1:
            FIRST_PLAYER_WINNER = True
            break
        elif game[line][line] == 2:
            SECOND_PLAYER_WINNER = True
            break

for col in range(3):
    counter1 = 0
    counter2 = 0
    for index in range(3):
        if game[index][col] == 1:
            counter1 += 1
        elif game[index][col] == 2:
            counter2 += 1
        if counter1 == 3:
            FIRST_PLAYER_WINNER = True
        elif counter2 == 3:
            SECOND_PLAYER_WINNER = True

if (game[0][0] == 1 and game[1][1] == 1 and game[2][2] == 1) or\
   (game[0][2] == 1 and game[1][1] == 1 and game[2][0] == 1):
    FIRST_PLAYER_WINNER = True
elif (game[0][0] == 2 and game[1][1] == 2 and game[2][2] == 2) or\
     (game[0][2] == 2 and game[1][1] == 2 and game[2][0] == 2):
    SECOND_PLAYER_WINNER = True

if FIRST_PLAYER_WINNER:
    print("First player won")
elif SECOND_PLAYER_WINNER:
    print("Second player won")
else:
    print("Draw!")

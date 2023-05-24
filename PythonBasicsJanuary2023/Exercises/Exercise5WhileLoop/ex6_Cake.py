pieces_cake = int(input()) * int(input())

guests_took = ''

while True:
    guests_took = input()

    if guests_took == "STOP":
        print(f'{pieces_cake} pieces are left.')
        break

    pieces_cake -= int(guests_took)

    if pieces_cake < 0:
        print(f'No more cake left! You need {abs(pieces_cake)} pieces more.')
        break

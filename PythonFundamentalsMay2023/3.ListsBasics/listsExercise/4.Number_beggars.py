coins_list = input().split(", ")
beggars_numbers = int(input())
total_offerings_per_beggar = []
index_beggar = 0

while index_beggar < beggars_numbers:
    beggar_gains = []

    for coin in range(index_beggar, len(coins_list), beggars_numbers):
        beggar_gains.append(int(coins_list[coin]))

    total_offerings_per_beggar.append(sum(beggar_gains))
    beggar_gains.clear()
    index_beggar += 1

print(total_offerings_per_beggar)

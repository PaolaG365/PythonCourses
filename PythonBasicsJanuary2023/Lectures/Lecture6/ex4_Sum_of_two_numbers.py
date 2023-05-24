start, end = int(input()), int(input())
magic_number = int(input())

count = 0
flag = False

for n1 in range(start, end + 1):
    for n2 in range(start, end + 1):
        count += 1

        if n1 + n2 == magic_number:
            flag = True
            print(f'Combination N:{count} ({n1} + {n2} = {magic_number})')
            break

    if flag:
        break

else:
    print(f'{count} combinations - neither equals {magic_number} ')

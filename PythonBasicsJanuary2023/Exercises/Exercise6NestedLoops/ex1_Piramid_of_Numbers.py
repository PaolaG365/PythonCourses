n = int(input())

current = 1
flag = False

for r in range(1, n + 1):
    for c in range(1, r + 1):

        if current > n:
            flag = True
            break
        print(current, end=' ')
        current += 1

    if flag:
        break
    print()
    
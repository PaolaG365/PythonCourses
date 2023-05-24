number = int(input())
counter = 0

for _ in range(number):
    symbols = input()

    if "(" in symbols:
        counter += 1

    if ")" in symbols:
        counter -= 1

    if 0 != counter != 1:
        print("UNBALANCED")
        break

else:
    print("BALANCED")

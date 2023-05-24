number = int(input())
list_number = list(str(number))

while True:
    number += 1
    if len(set(str(number))) == len(list_number):
        print(number)
        break

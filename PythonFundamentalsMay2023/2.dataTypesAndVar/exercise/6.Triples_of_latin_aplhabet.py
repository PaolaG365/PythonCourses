range_number = int(input())

for letter1 in range(97, 97 + range_number):
    for letter2 in range(97, 97 + range_number):
        for letter3 in range(97, 97 + range_number):
            print(f"{chr(letter1)}{chr(letter2)}{chr(letter3)}")

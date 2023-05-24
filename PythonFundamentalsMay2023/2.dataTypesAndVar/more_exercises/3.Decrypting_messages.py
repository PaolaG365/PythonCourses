key = int(input())
lines = int(input())
message = ''

for _ in range(lines):
    symbol = input()
    letter = ord(symbol) + key
    message += chr(letter)

print(message)

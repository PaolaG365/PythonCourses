message_to_cipher = input()
ciphered_message = ""

for char in message_to_cipher:
    ciphered_message += chr(ord(char) + 3)

print(ciphered_message)

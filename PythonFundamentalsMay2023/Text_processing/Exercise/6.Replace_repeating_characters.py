word = input()
last_symbol = ""
new_string = ""

for letter in word:
    if letter == last_symbol:
        continue
    else:
        new_string += letter
        last_symbol = letter

print(new_string)

symbols_string = input()
digits = ""
letters = ""
symbols = ""

for char in symbols_string:
    if not char.isalnum():
        symbols += char
    elif char.isdigit():
        digits += char
    elif char.isalpha():
        letters += char

print(digits, letters, symbols, sep="\n")

strings = input().lower().split()
counter_words = {}

for string in strings:
    if string in counter_words:
        counter_words[string] += 1
    else:
        counter_words[string] = 1

[print(f"{key}", end=" ") for key in counter_words if counter_words[key] % 2 != 0]

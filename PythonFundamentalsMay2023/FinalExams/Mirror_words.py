import re

valid_pairs_pattern = re.compile(r"(?P<sep>[@#])(?P<first_word>[A-Za-z]{3,})(?P=sep)"
                                 r"(?P=sep)(?P<second_word>[A-Za-z]{3,})(?P=sep)")

text = input()
pairs_found = re.finditer(valid_pairs_pattern, text)
palindrome_pairs = []

pairs = 0
for pair in pairs_found:
    pairs += 1
    if pair['first_word'] == pair['second_word'][::-1] and pair['first_word'][::-1] == pair['second_word']:
        palindrome_pairs.append(f"{pair['first_word']} <=> {pair['second_word']}")

if pairs > 0:
    print(f"{pairs} word pairs found!")
else:
    print("No word pairs found!")

if not palindrome_pairs:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(", ".join(palindrome_pairs))

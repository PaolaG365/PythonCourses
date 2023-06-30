word_synonyms = {}
lines = int(input())

for line in range(lines):
    word = input()
    synonym = input()
    if word in word_synonyms:
        word_synonyms[word].append(synonym)
    else:
        word_synonyms[word] = [synonym]

[print(f"{key} - {', '.join(word_synonyms[key])}") for key in word_synonyms]

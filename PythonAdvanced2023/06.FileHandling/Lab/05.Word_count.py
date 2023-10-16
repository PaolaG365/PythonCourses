import re

with open("words.txt", "r") as file:
    searched_words = file.read().lower().split()
with open("text1.txt", "r") as file:
    search_in = file.read().lower()

with open("result.txt", "w") as result:
    dict_result = {}
    for word in searched_words:
        search_for = rf"\b{word}\b"
        counts = len(re.findall(search_for, search_in))
        dict_result[word] = counts

    for word1, count in sorted(dict_result.items(), key=lambda x: -x[1]):
        result.write(f"{word1} - {count}\n")

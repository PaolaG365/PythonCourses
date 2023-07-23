import re

sentence = input()
search_word = input()
# pattern = fr"\b{search_word}\b"
word_list = re.findall(f"{search_word}\\b", sentence, re.IGNORECASE)
print(len(word_list))

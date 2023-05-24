lines = int(input())
special_word = input()
sentences = []
sorted_sentences = []

for line in range(lines):
    sentence = input()
    sentences.append(sentence)

    if special_word in sentence:
        sorted_sentences.append(sentence)

print(sentences)
print(sorted_sentences)

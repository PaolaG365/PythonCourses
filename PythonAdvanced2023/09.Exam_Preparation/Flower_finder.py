from collections import deque, defaultdict

flowers = ["rose", "tulip", "lotus", "daffodil"]
flowers_sets = {flower: set(flower) for flower in flowers}

vowels_collection = deque(input().split())
consonants_collection = deque(input().split())
word_found = False

while vowels_collection and consonants_collection:
    first_letter = vowels_collection.popleft()
    second_letter = consonants_collection.pop()

    for flower, letters in flowers_sets.items():
        letters.discard(first_letter)
        letters.discard(second_letter)
        if not letters:
            word_found = True
            print(f"Word found: {flower}")
            break

    if word_found:
        break
else:
    print("Cannot find any word!")

if vowels_collection:
    print(f"Vowels left: {' '.join(vowels_collection)}")
if consonants_collection:
    print(f"Consonants left: {' '.join(consonants_collection)}")

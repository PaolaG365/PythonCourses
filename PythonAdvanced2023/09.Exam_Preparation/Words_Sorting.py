def words_sorting(*words):
    dict_words = {}
    result = []
    for word in words:
        dict_words.setdefault(word, 0)
        dict_words[word] = sum(ord(char) for char in word)

    if sum(dict_words.values()) % 2 != 0:
        sorted_words = sorted(dict_words.items(), key=lambda x: -x[1])
    else:
        sorted_words = sorted(dict_words.items())

    for chars, value in sorted_words:
        result.append(f"{chars} - {value}")

    return '\n'.join(result)


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))
print()
print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))
print()
print(
    words_sorting(
        'cacophony',
        'accolade'
  ))
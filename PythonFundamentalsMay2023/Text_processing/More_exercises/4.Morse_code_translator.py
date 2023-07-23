morse_encoded_text = input().split(" | ")

MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..'}

decoded_message = []
morse_code_alphabet = list(MORSE_CODE_DICT.keys())
morse_code_values = list(MORSE_CODE_DICT.values())

for text in morse_encoded_text:
    decoded_word = ""
    word = text.split()
    for letter in word:
        index_letter = morse_code_values.index(letter)
        decoded_word += morse_code_alphabet[index_letter]

    decoded_message.append(decoded_word)

print(" ".join(decoded_message))

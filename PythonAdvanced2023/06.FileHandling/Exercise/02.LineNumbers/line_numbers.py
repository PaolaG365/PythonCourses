from string import punctuation, ascii_letters

with open("text.txt") as search_in_file, open("output.txt", "w") as result:
    results_list = []
    for line, content in enumerate(search_in_file.readlines()):
        n_letters = sum(content.count(letter) for letter in ascii_letters)
        n_punctuation = sum(content.count(sign) for sign in punctuation)
        results_list.append(f"Line {line + 1}: {content.strip()} ({n_letters})({n_punctuation})")
    result.write("\n".join(results_list))

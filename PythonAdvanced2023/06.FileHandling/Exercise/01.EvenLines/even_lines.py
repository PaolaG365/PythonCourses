target_punctuation = {"-", ",", ".", "!", "?"}

with open("text.txt") as file:
    for line, content in enumerate(file.readlines()):
        if line % 2 == 0:
            for sign in target_punctuation:
                content = content.replace(sign, "@")
            print(" ".join(content.split()[::-1]))

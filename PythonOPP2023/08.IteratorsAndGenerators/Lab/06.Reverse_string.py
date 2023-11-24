def reverse_text(text: str):
    start_index = len(text) - 1
    while start_index >= 0:
        yield text[start_index]
        start_index -= 1


for char in reverse_text("step"):
    print(char, end='')

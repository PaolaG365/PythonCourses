text = input()
stack = []

for index in range(len(text)):
    if text[index] == '(':
        stack.append(index)
    elif text[index] == ')':
        start_index = stack.pop()
        print(text[start_index:index + 1])

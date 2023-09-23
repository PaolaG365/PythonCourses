from collections import deque   # algorythm specific to exercise

parentheses = deque(input())
stack = []

if parentheses[0] not in "({[" or len(parentheses) % 2 != 0:
    print("NO")
    exit()

while parentheses:
    symbol = parentheses.popleft()
    if symbol in "({[":
        stack.append(symbol)
    elif f"{stack[-1] + symbol}" in "(){}[]":
        stack.pop()
    else:
        print("NO")
        break
else:
    print("YES")

text = list(input())
# stack = []
# for i in range(len(text)):
#     stack.append(text.pop())
# print("".join(stack))
for _ in range(len(text)):
    print(text.pop(), end="")
    
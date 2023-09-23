numbers_list = [int(n) for n in input().split()]
stack = []
for _ in range(len(numbers_list)):
    stack.append(numbers_list.pop())
print(*stack, sep=" ")

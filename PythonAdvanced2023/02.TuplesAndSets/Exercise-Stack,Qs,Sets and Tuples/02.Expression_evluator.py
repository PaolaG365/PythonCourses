from collections import deque
from math import floor

string_to_evaluate = deque(input().split())

while len(string_to_evaluate) > 1:
    nums = deque()
    operator = ""

    while string_to_evaluate:
        element = string_to_evaluate.popleft()
        if element.lstrip("-").isdigit():
            nums.append(int(element))
        else:
            operator = element
            break

    while len(nums) >= 2:
        num1 = nums.popleft()
        num2 = nums.popleft()
        result = 0
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            result = floor(num1 / num2)
        nums.appendleft(result)

    string_to_evaluate.appendleft(str(*nums))

print(*string_to_evaluate)

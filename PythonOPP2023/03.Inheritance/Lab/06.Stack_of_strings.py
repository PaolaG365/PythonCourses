from typing import List


class Stack:
    def __init__(self):
        self.data: List[str] = []

    def push(self, element):
        if isinstance(element, str):
            self.data.append(element)

    def pop(self):
        if self.data:
            return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        return f"[{', '.join(reversed(self.data))}]"


sample_stack = Stack()
print(sample_stack.push(1))
print(sample_stack.push("sad"))
print(sample_stack.push("happy"))
print(sample_stack.pop())
print(sample_stack.top())
print(sample_stack.is_empty())
sample_stack.pop()
print(sample_stack.is_empty())

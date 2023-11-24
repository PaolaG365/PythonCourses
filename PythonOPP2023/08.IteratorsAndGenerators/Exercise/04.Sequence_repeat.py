class sequence_repeat:
    def __init__(self, sequence: str, repeat: int):
        self.sequence = sequence
        self.repeat = repeat
        self.start = - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.repeat <= 0:
            raise StopIteration

        self.repeat -= 1
        self.start += 1
        return self.sequence[self.start % len(self.sequence)]


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')

print()

result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end='')

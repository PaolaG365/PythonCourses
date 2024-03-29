class reverse_iter:
    def __init__(self, iterable: list):
        self.iterable = iterable
        self.start = len(self.iterable)

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= 0:
            raise StopIteration

        self.start -= 1
        return self.iterable[self.start]


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)

class countdown_iterator:
    def __init__(self, count_n_to_0: int):
        self.count_n_to_0 = count_n_to_0 + 1
        self.end = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count_n_to_0 <= self.end:
            raise StopIteration

        self.count_n_to_0 -= 1
        return self.count_n_to_0


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
print()
iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")

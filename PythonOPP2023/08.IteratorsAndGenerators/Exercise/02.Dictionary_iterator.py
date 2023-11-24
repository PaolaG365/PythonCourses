class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.dictionary = tuple(dictionary.items())
        self.start = - len(self.dictionary) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= - 1:
            raise StopIteration

        self.start += 1
        return self.dictionary[self.start]


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

print()

result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)

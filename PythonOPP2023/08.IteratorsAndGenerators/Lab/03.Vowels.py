class vowels:
    def __init__(self, words: str):
        self.vowels = ["a", "e", "i", "u", "y", "o"]
        self.words = [char for char in words if char.lower() in self.vowels]
        self.end = len(self.words) - 1
        self.index = - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.end:
            raise StopIteration

        self.index += 1
        return self.words[self.index]


my_string = vowels('Hello World')
for char1 in my_string:
    print(char1)

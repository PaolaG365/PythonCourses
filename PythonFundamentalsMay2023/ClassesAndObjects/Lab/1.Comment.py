class Comment:
    def __init__(self, username, content, likes=0):
        self.username = username
        self.content = content
        self.likes = likes


comment = Comment("user12314", "I like this book, don't i", 10)
print(comment.username)
print(comment.content)
print(comment.likes)

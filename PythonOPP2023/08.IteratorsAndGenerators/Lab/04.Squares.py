def squares(n):
    square_num = 1
    while square_num < n + 1:
        yield square_num ** 2
        square_num += 1


print(list(squares(5)))

def row_prints(n, rows):  # not sure what this is for...
    print(" " * (n - rows), end="")
    print(*["*"] * rows)


def first_half(n):
    for row in range(1, n + 1):
        row_prints(n, row)


def second_half(n):
    for second_rows in range(n - 1, 0, -1):
        row_prints(n, second_rows)


def print_shape(rows_shape):
    first_half(rows_shape)
    second_half(rows_shape)


k = int(input())
print_shape(k)

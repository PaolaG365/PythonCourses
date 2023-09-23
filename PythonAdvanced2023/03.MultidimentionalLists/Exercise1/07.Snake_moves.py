from collections import deque

rows, cols = [int(x) for x in input().split()]

string_to_fill = deque(input())
matrix = []

for row in range(rows):
    matrix.append(['' for _ in range(cols)])
    for col in range(cols):
        if row % 2 == 0:
            matrix[row][col] = string_to_fill[0]
        else:
            matrix[row][- col - 1] = string_to_fill[0]
        string_to_fill.rotate(-1)

[print(''.join(line)) for line in matrix]

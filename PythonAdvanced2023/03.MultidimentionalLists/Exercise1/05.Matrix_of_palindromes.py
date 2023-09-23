rows, cols = [int(x) for x in input().split()]

start_ascii_el = ord("a")
matrix = []

for row in range(rows):
    inner_matrix = []
    for col in range(cols):
        inner_matrix.append(f"{chr(start_ascii_el)}{chr(start_ascii_el + col)}"
                            f"{chr(start_ascii_el)}")
    matrix.append(inner_matrix)
    start_ascii_el += 1

[print(*el) for el in matrix]

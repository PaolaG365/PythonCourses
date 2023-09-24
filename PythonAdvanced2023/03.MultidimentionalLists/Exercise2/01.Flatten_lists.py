input_string = input().split("|")
matrix = []
for substring in input_string:
    matrix.append([el.strip() for el in substring.split()])

matrix.reverse()
matrix = [el for row in matrix for el in row]
print(*matrix)

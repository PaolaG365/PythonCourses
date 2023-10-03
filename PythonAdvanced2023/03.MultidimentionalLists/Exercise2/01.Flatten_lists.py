input_string = input().split("|")
matrix = []
for substring in reversed(input_string):
    matrix.append([el for el in substring.split()])

matrix = [el for row in matrix for el in row]
print(*matrix)

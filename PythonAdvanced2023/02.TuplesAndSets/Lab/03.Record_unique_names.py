lines = int(input())
# unique_names = set(tuple(el for el in input().split()) for _ in range(lines))
# for name in unique_names:
#     print(*name)
unique_names = set()
for _ in range(lines):
    name = input()
    unique_names.add(name)

print(*unique_names, sep="\n")

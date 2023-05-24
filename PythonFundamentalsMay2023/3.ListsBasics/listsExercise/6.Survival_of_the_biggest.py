numbers_string = input()
count = int(input())

numbers_list = numbers_string.split(" ")
numbers_int = [int(x) for x in numbers_list]

for _ in range(count):
    min_num = min(numbers_int)
    numbers_int.remove(min_num)

print(*numbers_int, sep=", ")

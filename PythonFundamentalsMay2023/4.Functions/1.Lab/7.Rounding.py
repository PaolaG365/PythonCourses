def rounding(n):
    rounded = []
    for num in n:
        rounded.append(round(num))
    return rounded


first_list = input().split()
first_list = [float(x) for x in first_list]
print(list(rounding(first_list)))

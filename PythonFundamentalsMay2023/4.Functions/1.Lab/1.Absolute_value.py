def absolute_value(n):
    abs_list = []
    for num in n:
        abs_list.append(abs(num))
    return abs_list


nums = input().split()
nums = [float(x) for x in nums]
print(absolute_value(nums))

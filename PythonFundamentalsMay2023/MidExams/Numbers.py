list_of_numbers = [int(x) for x in input().split()]
average = sum(list_of_numbers) / len(list_of_numbers)
top_5_greater_than_avg = [num for num in list_of_numbers if num > average]

if top_5_greater_than_avg:
    top_5_greater_than_avg = sorted(top_5_greater_than_avg, reverse=True)
    if len(top_5_greater_than_avg) <= 5:
        print(*top_5_greater_than_avg)
    else:
        for index in range(5):
            print(top_5_greater_than_avg[index], end=" ")
else:
    print("No")

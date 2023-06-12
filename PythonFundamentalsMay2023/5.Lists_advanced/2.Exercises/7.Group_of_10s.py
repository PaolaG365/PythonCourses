def group_numbers_of_10s(numbers):
    groups_of_numbers = {}
    group = 10

    while numbers:
        numbers_in_group = [num for num in numbers if num <= group]
        numbers = [nums for nums in numbers if nums > group]
        groups_of_numbers.update({group: numbers_in_group})
        group += 10

    return groups_of_numbers


sequence_of_numbers = [int(x) for x in input().split(", ")]
groups_and_numbers = group_numbers_of_10s(sequence_of_numbers)

for groups in range(len(groups_and_numbers)):
    group_number = list(groups_and_numbers)[groups]
    numbers_into_group = list(groups_and_numbers.values())[groups]
    print(f"Group of {group_number}'s: {numbers_into_group}")

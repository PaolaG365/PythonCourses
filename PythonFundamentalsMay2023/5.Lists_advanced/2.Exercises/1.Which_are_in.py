first_list_of_strings = input().split(", ")
second_list_of_strings = input().split(", ")
print([s1 for s1 in first_list_of_strings if any(s1 in s2 for s2 in second_list_of_strings)])

#
# from_first_in_second = []
# for s1 in first_list_of_strings:
#     for s2 in second_list_of_strings:
#         if s1 in s2:
#             from_first_in_second.append(s1)
#             break
# print(from_first_in_second)

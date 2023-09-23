nums = tuple(input().split())
# nums_count = set(nums)
# # it's not wrong... it's just unordered <3
# for el in nums_count:
#     print(f"{float(el) if '.' in el else int(el):.1f} - {nums.count(el)} times.")

nums_dict = {}

for el in nums:
    counter_el = nums.count(el)
    if el not in nums_dict:
        print(f"{float(el) if '.' in el else int(el):.1f} - {counter_el} times")
    nums_dict[el] = counter_el

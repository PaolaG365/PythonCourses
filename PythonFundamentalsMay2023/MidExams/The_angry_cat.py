furniture_pricing = [int(x) for x in input().split(", ")]
jump_start = int(input())
items_type_to_destroy = input()

left_side = furniture_pricing[:jump_start]
right_side = furniture_pricing[jump_start + 1:]

if items_type_to_destroy == "cheap":
    left_side = [num for num in left_side if num < furniture_pricing[jump_start]]
    right_side = [num for num in right_side if num < furniture_pricing[jump_start]]
elif items_type_to_destroy == "expensive":
    left_side = [num for num in left_side if num >= furniture_pricing[jump_start]]
    right_side = [num for num in right_side if num >= furniture_pricing[jump_start]]

left_sum = sum(left_side)
right_sum = sum(right_side)

if right_sum > left_sum:
    print(f"Right - {right_sum}")
else:
    print(f"Left - {left_sum}")

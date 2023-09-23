lines = int(input())
longest_intersection = set()

for _ in range(lines):
    first_range, second_range = input().split("-")
    start1, end1 = [int(x) for x in first_range.split(",")]
    start2, end2 = [int(x) for x in second_range.split(",")]
    set1 = set([num for num in range(start1, end1 + 1)])
    set2 = set([num for num in range(start2, end2 + 1)])
    intersection = set1.intersection(set2)
    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

print(f"Longest intersection is [{', '.join(str(el) for el in longest_intersection)}] "
      f"with length {len(longest_intersection)}")

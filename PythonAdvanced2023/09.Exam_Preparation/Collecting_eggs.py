from collections import deque

BOX_SIZE = 50
boxes_counter = 0

eggs_sizes = deque(int(x) for x in input().split(", "))
paper_sizes = deque(int(x) for x in input().split(", "))

while eggs_sizes and paper_sizes:
    if eggs_sizes[0] == 13:
        eggs_sizes.popleft()
        paper_sizes[0], paper_sizes[-1] = paper_sizes[-1], paper_sizes[0]
        continue
    elif eggs_sizes[0] <= 0:
        eggs_sizes.popleft()
        continue
    egg = eggs_sizes.popleft()
    paper = paper_sizes.pop()
    if egg + paper <= BOX_SIZE:
        boxes_counter += 1

if boxes_counter > 0:
    print(f"Great! You filled {boxes_counter} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs_sizes:
    print(f"Eggs left: {', '.join(str(x) for x in eggs_sizes)}")
if paper_sizes:
    print(f"Pieces of paper left: {', '.join(str(x) for x in paper_sizes)}")

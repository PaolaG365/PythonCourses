sequence_numbers = input().split()
sequence_numbers = [float(x) for x in sequence_numbers]

left_side = sequence_numbers[:len(sequence_numbers)//2]
right_side = sequence_numbers[-1:-len(sequence_numbers)//2:-1]
left_side_timer = 0
right_side_timer = 0

for time1 in range(len(left_side)):
    left_side_timer += left_side[time1]
    if left_side[time1] == 0:
        left_side_timer *= 0.8

for time2 in range(len(right_side)):
    right_side_timer += right_side[time2]
    if right_side[time2] == 0:
        right_side_timer *= 0.8

if left_side_timer < right_side_timer:
    print(f"The winner is left with total time: {left_side_timer:.1f}")
else:
    print(f"The winner is right with total time: {right_side_timer:.1f}")

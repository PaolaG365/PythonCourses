from collections import deque

rubber_ducks_info = {
    "Darth Vader Ducky": [range(0, 61), 0],
    "Thor Ducky": [range(61, 121), 0],
    "Big Blue Rubber Ducky": [range(121, 181), 0],
    "Small Yellow Rubber Ducky": [range(181, 241), 0]
}

times_programmer = deque(int(x) for x in input().split())
task_times = deque(int(x) for x in input().split())

while times_programmer and task_times:
    programmer_time = times_programmer.popleft()
    time_task = task_times.pop()
    result = programmer_time * time_task

    for name, (duck_range, _) in rubber_ducks_info.items():
        if result in duck_range:
            rubber_ducks_info[name][1] += 1
            break
    # would work, task specific , we always get + nums
    else:
        times_programmer.append(programmer_time)
        task_times.append(time_task - 2)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
for duck, (_, count) in rubber_ducks_info.items():
    print(f"{duck}: {count}")

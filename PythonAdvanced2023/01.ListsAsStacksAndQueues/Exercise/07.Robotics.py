from collections import deque

robots_info = [x for x in input().split(";")]
open_hour, minutes, seconds = [int(x) for x in input().split(":")]
free_robots = {}
products = deque()
opening_time = open_hour * 3600 + minutes * 60 + seconds

for robot in robots_info:
    name_robot, time_processing = robot.split("-")
    free_robots.update({name_robot: {"time_processing": int(time_processing), "busy_until": 0}})

product = input()
while product != "End":
    products.append(product)
    product = input()

while products:
    opening_time += 1
    on_conveyr_product = products.popleft()
    for name, info in free_robots.items():
        if free_robots[name]['busy_until'] <= opening_time:
            hour = (opening_time // 3600) % 24
            minute = (opening_time % 3600) // 60
            second = (opening_time % 3600) % 60
            print(f"{name} - {on_conveyr_product} [{hour:02d}:{minute:02d}:{second:02d}]")
            info['busy_until'] = opening_time + info['time_processing']
            break
    else:
        products.append(on_conveyr_product)

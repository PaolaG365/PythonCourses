from collections import deque


food_quantity = int(input())
orders_q = deque([int(el) for el in input().split()])

print(max(orders_q))

while orders_q:
    order = orders_q[0]
    if food_quantity - order < 0:
        print("Orders left: ", end="")
        print(*orders_q, sep=" ")
        break
    else:
        orders_q.popleft()
        food_quantity -= order
else:
    print("Orders complete")

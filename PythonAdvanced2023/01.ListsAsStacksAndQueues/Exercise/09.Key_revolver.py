from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets_size = deque(int(x) for x in input().split())
locks_size = deque(int(x) for x in input().split())
intelligence_value = int(input())
bullets_counter, gun_barrel_counter = 0, gun_barrel_size

while True:
    if gun_barrel_counter == 0 and bullets_size:
        gun_barrel_counter = gun_barrel_size
        print("Reloading!")
        continue
    # it doesn't stop when you run of locks you gotta reload first i guess
    # it's only logical duh
    if not locks_size or not bullets_size:
        break

    lock = locks_size.popleft()
    bullet = bullets_size.pop()
    if bullet <= lock:
        print("Bang!")
    else:
        print("Ping!")
        locks_size.appendleft(lock)

    gun_barrel_counter -= 1
    bullets_counter += 1

if locks_size:
    print(f"Couldn't get through. Locks left: {len(locks_size)}")
else:
    print(f"{len(bullets_size)} bullets left. "
          f"Earned ${intelligence_value - (bullet_price * bullets_counter)}")

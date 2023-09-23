from collections import deque
kids_playing = deque(input().split())
rotation_number = int(input()) - 1

while len(kids_playing) > 1:
    kids_playing.rotate(-rotation_number)
    print(f"Removed {kids_playing.popleft()}")

print(f"Last is {kids_playing[0]}")

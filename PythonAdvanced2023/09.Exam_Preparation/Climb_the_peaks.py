from collections import deque

mountain_peaks = [
    ("Vihren", 80),
    ("Kutelo", 90),
    ("Banski Suhodol", 100),
    ("Polezhan", 60),
    ("Kamenitza", 70)
]

conquered_peaks = []
food_portions = deque(int(x) for x in input().split(", "))
stamina = deque(int(x) for x in input().split(", "))
days = 1

while days <= 7:
    if not stamina or not food_portions or not mountain_peaks:
        break

    daily_food = food_portions.pop()
    daily_stamina = stamina.popleft()
    result = daily_stamina + daily_food
    peak, height = mountain_peaks[0]

    if result >= height:
        conquered_peaks.append(peak)
        mountain_peaks.pop(0)
    else:
        continue

    days += 1

if not mountain_peaks:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered_peaks:
    print("Conquered peaks:")
    [print(peak) for peak in conquered_peaks]

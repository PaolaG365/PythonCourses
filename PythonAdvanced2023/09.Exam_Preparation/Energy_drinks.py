from collections import deque

milligrams_caffeine = deque(int(x) for x in input().split(", "))
energy_drinks = deque(int(x) for x in input().split(", "))
MAX_CAFFEINE = 300
REDUCTION_CAFFEINE = 30
total_caffeine = 0

while milligrams_caffeine and energy_drinks:
    current_caffeine = milligrams_caffeine.pop()
    current_energy_drink = energy_drinks.popleft()
    result = current_caffeine * current_energy_drink

    if total_caffeine + result <= MAX_CAFFEINE:
        total_caffeine += result
    else:
        energy_drinks.append(current_energy_drink)
        if total_caffeine - REDUCTION_CAFFEINE < 0:
            total_caffeine = 0
        else:
            total_caffeine -= REDUCTION_CAFFEINE

if energy_drinks:
    print(f"Drinks left: {', '.join(str(x) for x in energy_drinks)}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {total_caffeine} mg caffeine.")

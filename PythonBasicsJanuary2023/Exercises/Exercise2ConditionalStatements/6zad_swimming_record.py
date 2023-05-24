import math

world_record, distance, time_meter = float(input()), \
    float(input()), float(input())

without_resistance = distance * time_meter
counts_res = distance / 15
counts_res = math.floor(counts_res)
added_seconds = counts_res * 12.5
total_time = without_resistance + added_seconds

if total_time < world_record:
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')
else:
    a = total_time - world_record
    print(f'No, he failed! He was {a:.2f} seconds slower.')

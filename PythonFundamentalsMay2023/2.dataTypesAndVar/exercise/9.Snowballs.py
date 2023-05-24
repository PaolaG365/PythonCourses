snowballs_thrown = int(input())
weight_max = 0
time_max = 0
quality_max = 0
value_max = 0

for snowball in range(snowballs_thrown):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    snowball_value = (snowball_weight / snowball_time) ** snowball_quality

    if snowball_value > value_max:
        value_max = snowball_value
        weight_max = snowball_weight
        time_max = snowball_time
        quality_max = snowball_quality

print(f"{weight_max} : {time_max} = {int(value_max)} ({quality_max})")

import re

runners_list = input().split(", ")
runners_dict = {}
name = re.compile(r"(?i)[a-z]")
distance = re.compile(r"[0-9]")
command = input()

while command != "end of race":
    name_runner = re.findall(name, command)
    distance_runner = re.findall(distance, command)
    name_runner = "".join(name_runner)
    distance_runner = sum([int(x) for x in distance_runner])

    if name_runner in runners_list:
        if name_runner not in runners_dict:
            runners_dict[name_runner] = 0
        runners_dict[name_runner] += distance_runner

    command = input()

runners_dict = sorted(runners_dict.items(), key=lambda x: -x[1])

print(f"1st place: {runners_dict[0][0]}"
      f"\n2nd place: {runners_dict[1][0]}"
      f"\n3rd place: {runners_dict[2][0]}")

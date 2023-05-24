number_groups = int(input())

musala = 0
mont_blanc = 0
kilimanjaro = 0
k2 = 0
everest = 0
total_hikers = 0

for _ in range(number_groups):
    members_group = int(input())
    total_hikers += members_group
    if members_group < 6:
        musala += members_group
    elif members_group < 13:
        mont_blanc += members_group
    elif members_group < 26:
        kilimanjaro += members_group
    elif members_group < 41:
        k2 += members_group
    else:
        everest += members_group

print(f"{musala / total_hikers * 100:.2f}%")
print(f"{mont_blanc / total_hikers * 100:.2f}%")
print(f"{kilimanjaro / total_hikers * 100:.2f}%")
print(f"{k2 / total_hikers * 100:.2f}%")
print(f"{everest / total_hikers * 100:.2f}%")

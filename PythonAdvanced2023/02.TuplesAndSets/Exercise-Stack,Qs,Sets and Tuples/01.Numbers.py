set1 = {int(x) for x in input().split()}
set2 = {int(x) for x in input().split()}
actions_num = int(input())

actions_map = {
    "Add First": lambda x: set1.update(x),
    "Add Second": lambda x: [set2.add(item) for item in x],
    "Remove First": lambda x: [set1.discard(item) for item in x],
    "Remove Second": lambda x: [set2.discard(item) for item in x],
    "Check Subset": lambda x: print(set1.issubset(set2) or set2.issubset(set1))
}

for _ in range(actions_num):
    numbers_list = set()
    action = []
    for el in input().split():
        numbers_list.add(int(el)) if el.isdigit() else action.append(el)

    action = " ".join(action)
    actions_map[action](numbers_list)

print(*sorted(set1), sep=', ')
print(*sorted(set2), sep=', ')

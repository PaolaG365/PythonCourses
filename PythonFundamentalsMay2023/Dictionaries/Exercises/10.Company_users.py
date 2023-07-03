companies_dict = {}
command = input()

while command != "End":
    company, employee = command.split(" -> ")

    if company not in companies_dict:
        companies_dict[company] = []

    if employee not in companies_dict[company]:
        companies_dict[company].append(employee)

    command = input()

for corp in companies_dict:
    print(f"{corp}")
    for a_human_being in companies_dict[corp]:
        print(f"-- {a_human_being}")

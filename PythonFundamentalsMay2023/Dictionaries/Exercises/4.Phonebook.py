contact_numbers_dict = {}

while True:
    person_to_add_or_search = input()
    if person_to_add_or_search.isnumeric():
        break
    person, number = person_to_add_or_search.split("-")
    if person not in contact_numbers_dict:
        contact_numbers_dict[person] = ""
    contact_numbers_dict[person] = number

for human in range(int(person_to_add_or_search)):
    searched_person = input()
    if searched_person in contact_numbers_dict:
        print(f"{searched_person} -> {contact_numbers_dict[searched_person]}")
    else:
        print(f"Contact {searched_person} does not exist.")

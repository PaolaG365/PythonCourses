class Party:
    def __init__(self):
        self.people = []


party_instance = Party()
name_guest = input()

while name_guest != "End":
    party_instance.people.append(name_guest)
    name_guest = input()

print(f"Going: {', '.join(party_instance.people)}")
print(f"Total: {len(party_instance.people)}")

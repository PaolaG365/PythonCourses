guests_number = int(input())

VIPs = set()
peasants = set()

for _ in range(guests_number):
    reservation_code = input()
    if reservation_code[0].isdigit():
        VIPs.add(reservation_code)
    else:
        peasants.add(reservation_code)

party_guests = 0
present_guest_code = input()
while present_guest_code != "END":
    if present_guest_code in VIPs:
        VIPs.discard(present_guest_code)
    elif present_guest_code in peasants:
        peasants.discard(present_guest_code)
    party_guests += 1
    present_guest_code = input()

print(guests_number - party_guests)
if VIPs:
    vips_present = sorted(VIPs)
    print(*vips_present, sep='\n')
if peasants:
    peasants_present = sorted(peasants)
    print(*peasants_present, sep='\n')

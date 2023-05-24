period = int(input())

treated_patients = 0
untreated_patients = 0
docs_number = 7
patients_daily = 0

for day in range(1, period + 1):
    patients_incoming = int(input())

    if day % 3 == 0 and untreated_patients > treated_patients:
        docs_number += 1
    patients_daily = docs_number - patients_incoming

    if patients_incoming < docs_number:
        treated_patients += patients_incoming
    else:
        treated_patients += docs_number

    if patients_daily < 0:
        untreated_patients += abs(patients_daily)

print(f'Treated patients: {treated_patients}.\nUntreated patients: {untreated_patients}.')

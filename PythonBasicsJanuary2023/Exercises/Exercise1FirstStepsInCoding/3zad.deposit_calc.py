deposit = float(input())
deposit_term_in_moths = int(input())
yearly_percent = float(input()) / 100

sum_deposit = deposit + deposit_term_in_moths * ((deposit * yearly_percent) / 12)

print(sum_deposit)

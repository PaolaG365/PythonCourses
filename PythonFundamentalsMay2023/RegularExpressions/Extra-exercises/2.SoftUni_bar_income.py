import re

valid_income = re.compile(r"%(?P<name>[A-Z][a-z]+)%([^|$%.]*)"
                          r"<(?P<product>\w+)>([^|$%.]*)"
                          r"\|(?P<quantity>\d+)\|([^|$%.]*)"
                          r"(?P<price>[1-9]+[.0-9]+)\$")

command = input()
total_income = 0

while command != "end of shift":
    match = re.search(valid_income, command)
    if match:
        customer_bill = match.groupdict()
        total_customer = int(customer_bill['quantity']) * float(customer_bill['price'])
        total_income += total_customer
        print(f"{customer_bill['name']}: {customer_bill['product']} - {total_customer:.2f}")

    command = input()

print(f"Total income: {total_income:.2f}")

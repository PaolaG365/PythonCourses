import re

barcodes_to_check = int(input())
barcode_pattern = re.compile(r"@#+(?P<item>[A-Z][A-Za-z0-9]{4,}[A-Z])@#+")

for _ in range(barcodes_to_check):
    barcode = input()
    valid_barcode = re.search(barcode_pattern, barcode)
    if valid_barcode:
        string_to_check = valid_barcode.group()
        product_group = [x for x in string_to_check if x.isdigit()]
        if not product_group:
            product_group = ['0'] * 2
        print(f"Product group: {''.join(product_group)}")
    else:
        print("Invalid barcode")

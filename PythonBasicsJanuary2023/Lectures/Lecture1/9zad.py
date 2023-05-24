square_meters_of_house = float(input())

PRICE_PER_SQUARE_METER = 7.61
DISCOUNT_FROM_TOTAL_PRICE = 0.18

price_without_discount = square_meters_of_house * PRICE_PER_SQUARE_METER

discount = price_without_discount * DISCOUNT_FROM_TOTAL_PRICE

final_price = price_without_discount - discount

print(f'The final price is: {final_price} lv.')
print(f'The discount is: {discount} lv.')

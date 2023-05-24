pens_packs = int(input())
marker_packs = int(input())
detergent_liters = int(input())
discount = int(input()) / 100

PEN_PRICE = 5.80
MARKER_PRICE = 7.20
DETERGENT_PRICE = 1.20

price_before_discount = (pens_packs * PEN_PRICE) + (marker_packs * MARKER_PRICE) + (detergent_liters * DETERGENT_PRICE)
total_price = price_before_discount - price_before_discount * discount

print(total_price)

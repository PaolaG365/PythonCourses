mackerel_price = float(input())
sprinkle_price = float(input())
bonito_in_kg = float(input())
safrid_in_kg = float(input())
mussels_in_kg = int(input())

bonito = mackerel_price + mackerel_price * 0.6
safrid = sprinkle_price + sprinkle_price * 0.8
MUSSELS = 7.50

total_price = bonito_in_kg * bonito + safrid_in_kg * safrid + mussels_in_kg * MUSSELS
print(f'{total_price:.2f}')

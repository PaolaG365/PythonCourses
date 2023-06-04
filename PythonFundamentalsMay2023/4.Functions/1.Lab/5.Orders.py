def total_price(quantity, type=""):
    prices_glossary = {"coffee": 1.50, "water": 1.00, "coke": 1.40, "snacks": 2.00}
    price_one = float(prices_glossary.get(type))
    result = price_one * quantity
    return result


order = input()
count = int(input())
print(f"{total_price(count, type=order):.2f}")

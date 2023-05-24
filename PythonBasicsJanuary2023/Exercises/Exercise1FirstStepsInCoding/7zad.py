chicken_menus = int(input())
fish_menus = int(input())
vegetarian_menus = int(input())

CHICKEN_MENU_PRICE = 10.35
FISH_MENU_PRICE = 12.40
VEGETARIAN_MENU_PRICE = 8.15
DELIVERY = 2.50

total_menus_price = chicken_menus * CHICKEN_MENU_PRICE + fish_menus * FISH_MENU_PRICE\
    + vegetarian_menus * VEGETARIAN_MENU_PRICE
dessert = total_menus_price * 0.20
total = total_menus_price + dessert + DELIVERY

print(total)

from typing import Dict


class Shop:
    def __init__(self, name: str, _type: str, capacity: int):
        self.name = name
        self.type = _type
        self.capacity = capacity
        self.items: Dict[str: int] = {}

    @classmethod
    def small_shop(cls, name: str, _type: str):
        return cls(name, _type, 10)

    def add_item(self, item: str):
        if sum(self.items.values()) >= self.capacity:
            return "Not enough capacity in the shop"
        self.items.setdefault(item, 0)
        self.items[item] += 1
        return f"{item} added to the shop"

    def remove_item(self, item: str, amount: int):
        if item not in self.items or self.items[item] < amount:
            return f"Cannot remove {amount} {item}"
        self.items[item] -= amount
        if self.items[item] <= 0:
            del self.items[item]
        return f"{amount} {item} removed from the shop"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"


fresh_shop = Shop("Fresh Shop", "Fruit and Veg", 50)
small_shop = Shop.small_shop("Fashion Boutique", "Clothes")
print(fresh_shop)
print(small_shop)

print(fresh_shop.add_item("Bananas"))
print(fresh_shop.remove_item("Tomatoes", 2))

print(small_shop.add_item("Jeans"))
print(small_shop.add_item("Jeans"))
print(small_shop.remove_item("Jeans", 2))
print(small_shop.items)

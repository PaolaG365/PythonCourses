from typing import List
from product import Product


class ProductRepository:
    def __init__(self):
        self.products: List[Product] = []

    def add(self, product: Product) -> None:
        self.products.append(product)

    def find(self, product_name: str) -> Product:
        for product in self.products:
            if product.name == product_name:
                return product

    def remove_item(self, product_name: str) -> None:
        target_product = self.find(product_name)
        if target_product:
            self.products.remove(target_product)

    def __repr__(self):
        products_data = [f"{product.name}: {product.quantity}" for product in self.products]
        return "\n".join(products_data)

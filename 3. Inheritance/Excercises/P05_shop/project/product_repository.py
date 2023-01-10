from project.drink import Drink
from project.food import Food
from project.product import Product


class ProductRepository:

    def __init__(self):
        self.products = list()

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for product in self.products:
            if product.name == product_name:
                return product

    def remove(self, product_name):
        product = self.find(product_name)
        if product is not None:
            self.products.remove(product)

    def __repr__(self):
        result = ""
        for product in self.products:
            result += f"{product.name}: {product.quantity}\n"

        return result.strip()


food = Food("apple")
drink = Drink("water")
repo = ProductRepository()
repo.add(food)
repo.add(drink)
print(repo.products)
print(repo.find("water"))
repo.find("apple").decrease(5)
print(repo)



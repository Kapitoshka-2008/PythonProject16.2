from abc import ABC, abstractmethod
from typing import List


class CreationLoggerMixin:
    def __init__(self, *args, **kwargs):
        print(f"Создан объект {self.__class__.__name__} с параметрами: {args}, {kwargs}")
        super().__init__(*args, **kwargs)


class BaseProduct(ABC):
    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Product(CreationLoggerMixin, BaseProduct):
    def __init__(self, name: str, description: str, price: float, quantity: int):
        super().__init__(name, description, price, quantity)


class Smartphone(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 performance: str, model: str, memory: str, color: str):
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country: str, germination_period: str, color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: List[Product]):
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.product_count += len(products) 
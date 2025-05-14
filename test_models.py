import pytest
from models import Product, Category, Smartphone, LawnGrass


def test_product_creation():
    product = Product("Test Product", "Test Description", 100.0, 5)
    assert product.name == "Test Product"
    assert product.description == "Test Description"
    assert product.price == 100.0
    assert product.quantity == 5


def test_smartphone_creation():
    smartphone = Smartphone("Test Phone", "Test Description", 100.0, 5,
                           "High", "Model X", "256GB", "Black")
    assert smartphone.name == "Test Phone"
    assert smartphone.performance == "High"
    assert smartphone.model == "Model X"
    assert smartphone.memory == "256GB"
    assert smartphone.color == "Black"


def test_lawn_grass_creation():
    grass = LawnGrass("Test Grass", "Test Description", 100.0, 5,
                      "USA", "2 weeks", "Green")
    assert grass.name == "Test Grass"
    assert grass.country == "USA"
    assert grass.germination_period == "2 weeks"
    assert grass.color == "Green"


def test_category_creation():
    product = Product("Test Product", "Test Description", 100.0, 5)
    category = Category("Test Category", "Test Description", [product])
    assert category.name == "Test Category"
    assert len(category.products) == 1
    assert Category.category_count > 0
    assert Category.product_count > 0


def test_category_counters():
    initial_category_count = Category.category_count
    initial_product_count = Category.product_count
    
    product1 = Product("Test Product 1", "Test Description", 100.0, 5)
    product2 = Product("Test Product 2", "Test Description", 200.0, 10)
    
    category = Category("Test Category", "Test Description", [product1, product2])
    
    assert Category.category_count == initial_category_count + 1
    assert Category.product_count == initial_product_count + 2 
import pytest
from models import Product, Category, Smartphone, LawnGrass, BaseProduct


def test_base_product_abstract():
    """Тест проверяет, что BaseProduct является абстрактным классом"""
    with pytest.raises(TypeError):
        BaseProduct("Test", "Test", 100.0, 5)


def test_product_creation():
    """Тест проверяет создание базового продукта"""
    product = Product("Test Product", "Test Description", 100.0, 5)
    assert product.name == "Test Product"
    assert product.description == "Test Description"
    assert product.price == 100.0
    assert product.quantity == 5


def test_product_str():
    """Тест проверяет строковое представление продукта"""
    product = Product("Test Product", "Test Description", 100.0, 5)
    expected_str = "Test Product, 100.0 руб. Остаток: 5 шт."
    assert str(product) == expected_str


def test_product_repr():
    """Тест проверяет repr представление продукта"""
    product = Product("Test Product", "Test Description", 100.0, 5)
    expected_repr = "Product(Test Product, Test Description, 100.0, 5)"
    assert repr(product) == expected_repr


def test_smartphone_creation():
    """Тест проверяет создание смартфона"""
    smartphone = Smartphone("Test Phone", "Test Description", 100.0, 5,
                           "High", "Model X", "256GB", "Black")
    assert smartphone.name == "Test Phone"
    assert smartphone.performance == "High"
    assert smartphone.model == "Model X"
    assert smartphone.memory == "256GB"
    assert smartphone.color == "Black"


def test_smartphone_str():
    """Тест проверяет строковое представление смартфона"""
    smartphone = Smartphone("Test Phone", "Test Description", 100.0, 5,
                           "High", "Model X", "256GB", "Black")
    expected_str = "Test Phone, 100.0 руб. Остаток: 5 шт.\nПроизводительность: High, Модель: Model X, Память: 256GB, Цвет: Black"
    assert str(smartphone) == expected_str


def test_smartphone_repr():
    """Тест проверяет repr представление смартфона"""
    smartphone = Smartphone("Test Phone", "Test Description", 100.0, 5,
                           "High", "Model X", "256GB", "Black")
    expected_repr = "Smartphone(Test Phone, Test Description, 100.0, 5, High, Model X, 256GB, Black)"
    assert repr(smartphone) == expected_repr


def test_lawn_grass_creation():
    """Тест проверяет создание газонной травы"""
    grass = LawnGrass("Test Grass", "Test Description", 100.0, 5,
                      "USA", "2 weeks", "Green")
    assert grass.name == "Test Grass"
    assert grass.country == "USA"
    assert grass.germination_period == "2 weeks"
    assert grass.color == "Green"


def test_lawn_grass_str():
    """Тест проверяет строковое представление газонной травы"""
    grass = LawnGrass("Test Grass", "Test Description", 100.0, 5,
                      "USA", "2 weeks", "Green")
    expected_str = "Test Grass, 100.0 руб. Остаток: 5 шт.\nСтрана: USA, Период прорастания: 2 weeks, Цвет: Green"
    assert str(grass) == expected_str


def test_lawn_grass_repr():
    """Тест проверяет repr представление газонной травы"""
    grass = LawnGrass("Test Grass", "Test Description", 100.0, 5,
                      "USA", "2 weeks", "Green")
    expected_repr = "LawnGrass(Test Grass, Test Description, 100.0, 5, USA, 2 weeks, Green)"
    assert repr(grass) == expected_repr


def test_category_creation():
    """Тест проверяет создание категории"""
    product = Product("Test Product", "Test Description", 100.0, 5)
    category = Category("Test Category", "Test Description", [product])
    assert category.name == "Test Category"
    assert len(category.products) == 1
    assert Category.category_count > 0
    assert Category.product_count > 0


def test_category_str():
    """Тест проверяет строковое представление категории"""
    product = Product("Test Product", "Test Description", 100.0, 5)
    category = Category("Test Category", "Test Description", [product])
    expected_str = "Test Category, количество продуктов: 1 шт."
    assert str(category) == expected_str


def test_category_repr():
    """Тест проверяет repr представление категории"""
    product = Product("Test Product", "Test Description", 100.0, 5)
    category = Category("Test Category", "Test Description", [product])
    expected_repr = "Category(Test Category, Test Description, [Product(Test Product, Test Description, 100.0, 5)])"
    assert repr(category) == expected_repr


def test_category_counters():
    """Тест проверяет счетчики категорий и продуктов"""
    initial_category_count = Category.category_count
    initial_product_count = Category.product_count
    
    product1 = Product("Test Product 1", "Test Description", 100.0, 5)
    product2 = Product("Test Product 2", "Test Description", 200.0, 10)
    
    category = Category("Test Category", "Test Description", [product1, product2])
    
    assert Category.category_count == initial_category_count + 1
    assert Category.product_count == initial_product_count + 2


def test_inheritance_chain():
    """Тест проверяет цепочку наследования"""
    assert issubclass(Product, BaseProduct)
    assert issubclass(Smartphone, Product)
    assert issubclass(LawnGrass, Product)
    assert not issubclass(Product, Smartphone)
    assert not issubclass(Product, LawnGrass)


def test_mixin_logging(capsys):
    """Тест проверяет работу миксина логирования"""
    product = Product("Test Product", "Test Description", 100.0, 5)
    captured = capsys.readouterr()
    assert "Создан объект Product" in captured.out
    assert "Test Product" in captured.out
    assert "Test Description" in captured.out
    assert "100.0" in captured.out
    assert "5" in captured.out 
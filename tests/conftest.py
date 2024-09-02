import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def first_product() -> Product:
    return Product(name="Apple Iphone 15", description="Смартфон", price=65000, quantity=5)


@pytest.fixture
def first_category() -> Category:
    return Category(
        name="Смартфоны",
        description="Смартфоны",
        products=[
            Product("Apple Iphone 15", "Смартфон", 65000, 5),
            Product("Samsung Galaxy S24", "Смартфон", 60000, 3),
        ],
    )


@pytest.fixture
def second_category() -> Category:
    return Category(
        name="Телевизоры",
        description="Телевизоры",
        products=[
            Product("Samsung UE43DU7100", "Телевизор", 41000, 4),
            Product("Xiaomi MI TV A Pro 43", "Телевизор", 35000, 2),
            Product("Sony KD-32W830K", "Телевизор", 43000, 3),
        ],
    )


@pytest.fixture
def products_by_category_list() -> list:
    return [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, как средство не только коммуникации, "
            "но и получение дополнительных функций для удобства жизни",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5,
                },
                {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
                {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14},
            ],
        },
        {
            "name": "Телевизоры",
            "description": "Современный телевизор, который позволяет наслаждаться просмотром, "
            "станет вашим другом и помощником",
            "products": [
                {"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
            ],
        },
    ]


@pytest.fixture
def product_dict():
    return {"name": "Test Product", "description": "Test description", "price": 100, "quantity": 1}


@pytest.fixture
def products_list():
    return [
        Product("Test Product", "Test description", 150, 1),
        Product("Other Product", "Test description", 200, 1)
    ]

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

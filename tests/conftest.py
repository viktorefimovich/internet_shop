import pytest

from src.product import Product
from src.category import Category


@pytest.fixture
def first_product():
    return Product(
        name="Apple Iphone 15",
        description="Смартфон",
        price=65000,
        quantity=5
    )

@pytest.fixture
def second_product():
    return Product(
        name="Samsung Galaxy S24",
        description="Смартфон",
        price=60000,
        quantity=3
    )

@pytest.fixture
def first_category():
    return Category(
        name="Смартфоны",
        description="Смартфоны",
        products=[
            Product("Apple Iphone 15", "Смартфон", 65000, 5),
            Product("Samsung Galaxy S24", "Смартфон", 60000, 3)
        ]
    )

@pytest.fixture
def second_category():
    return Category(
        name="Телевизоры",
        description="Телевизоры",
        products=[
            Product("Samsung UE43DU7100", "Телевизор", 41000, 4),
            Product("Xiaomi MI TV A Pro 43", "Телевизор", 35000, 2),
            Product("Sony KD-32W830K", "Телевизор", 43000, 3)
        ]
    )
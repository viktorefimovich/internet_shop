import pytest

from src.category import Category
from src.product import Product
from src.product_iterator import ProductIterator
from src.product_lawngrass import LawnGrass
from src.product_smartphone import Smartphone


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
def product1() -> Product:
    return Product(
        name="Samsung Galaxy S23 Ultra", description="256GB, Серый цвет, 200MP камера", price=180000.0, quantity=5
    )


@pytest.fixture
def product2() -> Product:
    return Product(name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8)


@pytest.fixture
def product3() -> Product:
    return Product(name="Xiaomi Redmi Note 11", description="1024GB, Синий", price=31000.0, quantity=14)


@pytest.fixture
def product4() -> Product:
    return Product(name='55" QLED 4K', description="Фоновая подсветка", price=123000.0, quantity=7)


@pytest.fixture
def category1(product1: Product, product2: Product, product3: Product) -> Category:
    return Category(
        name="Смартфоны",
        description="""
        Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни
        """,
        products=[product1, product2, product3],
    )


@pytest.fixture
def category2(product4: Product) -> Category:
    return Category(
        name="Телевизоры",
        description="""
        Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником
        """,
        products=[product4],
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
def product_dict() -> dict:
    return {"name": "Test Product", "description": "Test description", "price": 100, "quantity": 1}


@pytest.fixture
def products_list() -> list:
    return [Product("Test Product", "Test description", 150, 1), Product("Other Product", "Test description", 200, 1)]


@pytest.fixture
def product_iterator(category1: Category) -> ProductIterator:
    return ProductIterator(category1)


@pytest.fixture
def smartphone1() -> Smartphone:
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def smartphone2() -> Smartphone:
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def smartphone3() -> Smartphone:
    return Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")


@pytest.fixture
def grass1() -> LawnGrass:
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def grass2() -> LawnGrass:
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")


@pytest.fixture
def category_without_products():
    return Category(
        name="Смартфоны",
        description="""Смартфоны, как средство не только коммуникации, 
но и получения дополнительных функций для удобства жизни""",
        products=[],
    )

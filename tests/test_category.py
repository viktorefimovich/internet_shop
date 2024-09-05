import pytest

from src.category import Category
from src.product import Product


def test_category_init(first_category: Category, second_category: Category) -> None:
    assert first_category.name == "Смартфоны"
    assert first_category.description == "Смартфоны"
    assert len(first_category.products_list) == 2

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 5
    assert second_category.product_count == 5


def test_category_products(first_category: Category) -> None:
    assert (
        first_category.products == "Apple Iphone 15, 65000 руб. Остаток: 5 шт.\n"
        "Samsung Galaxy S24, 60000 руб. Остаток: 3 шт.\n"
    )


def test_add_product(first_category: Category, first_product: Product) -> None:
    category = first_category
    category.add_product(first_product)
    assert category.products_list[-1] == first_product
    assert Category.product_count == 10


def test_category_str(category2: Category) -> None:
    result = str(category2)
    assert result == "Телевизоры, количество продуктов: 7 шт."


def test_category_add_product_error(category2):
    with pytest.raises(TypeError):
        assert category2.add_product("Это не продукт")

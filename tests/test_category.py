from src.category import Category


def test_category_init(first_category: Category, second_category: Category) -> None:
    assert first_category.name == "Смартфоны"
    assert first_category.description == "Смартфоны"
    assert len(first_category.products_list) == 2

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 5
    assert second_category.product_count == 5


def test_category_products(first_category):
    assert (first_category.products == "Apple Iphone 15, 65000 руб. Остаток: 5 шт.\n"
                                       "Samsung Galaxy S24, 60000 руб. Остаток: 3 шт.\n")


def test_add_product(first_category, first_product):
    category = first_category
    category.add_product(first_product)
    assert category.products_list[-1] == first_product
    assert Category.product_count == 10

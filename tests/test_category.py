from src.category import Category


def test_category_init(first_category: Category, second_category: Category) -> None:
    assert first_category.name == "Смартфоны"
    assert first_category.description == "Смартфоны"
    assert len(first_category.products) == 2

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 5
    assert second_category.product_count == 5

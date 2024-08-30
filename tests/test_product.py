from src.product import Product


def test_product_init(first_product: Product) -> None:
    assert first_product.name == "Apple Iphone 15"
    assert first_product.description == "Смартфон"
    assert first_product.price == 65000
    assert first_product.quantity == 5

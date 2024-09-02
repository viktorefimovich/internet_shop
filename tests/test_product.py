from src.product import Product


def test_product_init(first_product: Product) -> None:
    assert first_product.name == "Apple Iphone 15"
    assert first_product.description == "Смартфон"
    assert first_product.price == 65000
    assert first_product.quantity == 5


def test_positive_price(first_product):
    price_temp = first_product
    price_temp.price = 90000
    assert first_product.price == 90000


def test_negative_price(first_product, capsys):
    price_temp = first_product
    price_temp.price = 0
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-1] == "Цена не должна быть нулевая или отрицательная"


def test_smaller_price_y(first_product, monkeypatch):
    price_temp = first_product

    monkeypatch.setattr('builtins.input', lambda _: "y")
    price_temp.price = 60000
    assert price_temp.price == 60000


def test_smaller_price_n(first_product, monkeypatch, capsys):
    price_temp = first_product

    monkeypatch.setattr('builtins.input', lambda _: "n")
    price_temp.price = 60000
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-1] == "Цена не изменена"


def test_new_product_without_products_list(product_dict):
    new_product = Product.new_product(product_dict)
    assert new_product.name == "Test Product"
    assert new_product.price == 100
    assert new_product.quantity == 1


def test_new_product_with_products_list(product_dict, products_list):
    new_product = Product.new_product(product_dict, products_list)
    assert new_product.name == "Test Product"
    assert new_product.price == 150
    assert new_product.quantity == 2

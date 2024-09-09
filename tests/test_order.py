from src.order import Order
from src.product import Product


def test_order(product1: Product) -> None:
    assert str(Order(product1, 2)) == "Было приобретено: Samsung Galaxy S23 Ultra - 2 шт., на общую сумму 360000.0"

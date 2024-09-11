from _pytest.capture import CaptureFixture

from src.order import Order
from src.product import Product


def test_order(product1: Product) -> None:
    assert str(Order(product1, 2)) == "Было приобретено: Samsung Galaxy S23 Ultra - 2 шт., на общую сумму 360000.0"


def test_custom_exception(capsys: CaptureFixture[str], product4: Product) -> None:
    product4.quantity = 0
    Order(product4, 2)
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-2] == "Товар с нулевым количеством добавить в заказ нельзя"
    assert message.out.strip().split("\n")[-1] == "Обработка добавления товара в заказ завершена"

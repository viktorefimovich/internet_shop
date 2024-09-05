import pytest

from src.product import Product
from src.product_smartphone import Smartphone


def test_smartphone_init(smartphone1: Smartphone) -> None:
    assert smartphone1.color == "Серый"


def test_smartphone_add(smartphone2: Smartphone, smartphone3: Smartphone) -> None:
    assert smartphone2 + smartphone3 == 2114000


def test_smartphone_add_error(smartphone1: Smartphone, product2: Product) -> None:
    with pytest.raises(TypeError):
        assert smartphone1 + product2

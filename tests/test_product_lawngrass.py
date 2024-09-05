import pytest

from src.product import Product
from src.product_lawngrass import LawnGrass


def test_lawn_grass_init(grass1: LawnGrass) -> None:
    assert grass1.color == "Зеленый"


def test_lawn_grass_add(grass1: LawnGrass, grass2: LawnGrass) -> None:
    assert grass1 + grass2 == 16750


def test_lawn_grass_add_error(grass1: LawnGrass, product2: Product) -> None:
    with pytest.raises(TypeError):
        assert grass1 + product2

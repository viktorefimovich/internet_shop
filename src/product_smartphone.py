from typing import Any

from src.product import Product


class Smartphone(Product):
    """Класс смартфоны, отдельно существующий продукт"""

    name: str
    description: str
    __price: float
    quantity: int
    efficiency: float
    model: str
    memory: int
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        """Метод для инициализации экземпляра класса"""

        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other: Any) -> Any:
        """Магический метод для вычисления полной стоимости всех товаров на складе одной категории"""

        if type(other) is Smartphone:
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise TypeError

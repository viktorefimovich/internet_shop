from typing import Any


class Product:
    """Класс для представления продукта"""

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Метод для инициализации экземпляра класса"""

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self) -> str:
        """Магический метод для строкового отображения для класса Product"""

        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Any) -> Any:
        """Магический метод для вычисления полной стоимости всех товаров на складе"""

        return self.__price * self.quantity + other.__price * other.quantity

    @property
    def price(self) -> float:
        """Геттер для вывода цены"""

        return self.__price

    @price.setter
    def price(self, price: float) -> None:
        """Сеттер для записи новой цены"""

        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif self.__price > price:
            answer = input("Снизить цену? y/n: ").lower()
            if answer == "y":
                self.__price = price
            else:
                print("Цена не изменена")
        else:
            self.__price = price

    @classmethod
    def new_product(cls, product_dict: dict, products_list: list | None = None) -> Any:
        """Класс-метод, который принимает на вход параметры товара в словаре и возвращает объект класса Product"""

        if products_list is None:
            return cls(**product_dict)
        for product in products_list:
            if product_dict["name"] == product.name:
                product_dict["quantity"] += product.quantity
                if product.price > product_dict["price"]:
                    product_dict["price"] = product.price
        return cls(**product_dict)

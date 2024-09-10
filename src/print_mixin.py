class PrintMixin:
    """Класс-миксин для печати в консоль информации о том, от какого класса и с какими параметрами был создан объект"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self) -> None:
        print(repr(self))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"

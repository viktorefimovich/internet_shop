from typing import Any, Iterator

from src.category import Category


class ProductIterator:
    """Класс, с помощью которого можно перебирать товары одной категории"""

    category_products: Category
    index: int

    def __init__(self, category_products: Category):
        """Метод для инициализации экземпляра класса"""

        self.category_products = category_products

    def __iter__(self) -> Iterator:
        """Магический метод для получения итератора"""

        self.index = 0
        return self

    def __next__(self) -> Any:
        """Магический мнтод для перехода к следующему значению и его считывание"""

        if self.index < len(self.category_products.products_list):
            product = self.category_products.products_list[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration

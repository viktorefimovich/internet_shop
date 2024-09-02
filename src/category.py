from src.product import Product


class Category:
    """Класс для представления категорий"""

    name: str
    description: str
    __products: list
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        """Метод для инициализации экземпляра класса"""

        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    @property
    def products(self) -> str:
        """Геттер для вывода списка товаров в виде строки"""

        result = ""
        for product in self.__products:
            result += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return result

    def add_product(self, product: Product) -> None:
        """Метод для добавления товаров в категорию"""

        self.__products.append(product)
        Category.product_count += 1

#quantity of requested products
QUANTITY_OF_REQUESTED_PRODUCTS = 999 #количество запрашиваемой продукции

#@dataclass #dataclass говорит, что абстракция USERS это абстракция над данными, а если это данные, мы можем совершать операции (и не нужно писать функции сравнения и т.п.)
class Product:
    """
    Класс продукта (есть некий продукт)
    """
    name: str #имя
    price: float #цена
    description: str #описание
    quantity: int #количество

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    def check_quantity(self, quantity) -> bool: #проверка количества, если кол-во товара достаточное, то TRUE, если нет, то FALSE
        return self.quantity >= quantity #метод будет возвращать True, если количество товара на складе (self.quantity) больше или равно запрошенному количеству (quantity), и False в противном случае.
        """
        TODO Верните True если количество продукта больше или равно запрашиваемому
            и False в обратном случае
        """
        raise NotImplementedError

    def buy(self, quantity): #покупка - вычитает какое-то кол-во товара, которое лежит на складе
        """
        TODO реализуйте метод покупки
            Проверьте количество продукта используя метод check_quantity
            Если продуктов не хватает, то выбросите исключение ValueError
        """
        raise NotImplementedError

    #def __hash__(self):
    #   return hash(self.name + self.description)


class Cart:
    """
    Класс корзины. В нем хранятся продукты, которые пользователь хочет купить.
    TODO реализуйте все методы класса
    """

    # Словарь продуктов и их количество в корзине
    products: dict[Product, int]

    def __init__(self):
        # По-умолчанию корзина пустая
        self.products = {}

    def add_product(self, product: Product, buy_count=1):
        """
        Метод добавления продукта в корзину.
        Если продукт уже есть в корзине, то увеличиваем количество
        """
        raise NotImplementedError

    def remove_product(self, product: Product, remove_count=None):
        """
        Метод удаления продукта из корзины.
        Если remove_count не передан, то удаляется вся позиция
        Если remove_count больше, чем количество продуктов в позиции, то удаляется вся позиция
        """
        raise NotImplementedError

    def clear(self): #очистить всю корзину
        raise NotImplementedError

    def get_total_price(self) -> float: #можешь посчитать цену всех товаров в корзине
        raise NotImplementedError

    def buy(self): #можем купить все товары в корзине
        """
        Метод покупки.
        Учтите, что товаров может не хватать на складе.
        В этом случае нужно выбросить исключение ValueError
        """
        raise NotImplementedError
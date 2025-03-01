QUANTITY_OF_REQUESTED_PRODUCTS = 800

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

    def check_quantity(self, quantity) -> bool:
        return (quantity <= self.quantity)
        """
        TODO Верните True если количество продукта больше или равно запрашиваемому
            и False в обратном случае
        """

    def buy(self, quantity):
        if self.check_quantity(quantity): #если выполняются условия функции
            self.quantity -= quantity # то количество товара на складе уменьшается на количество купленного товара
            return self.quantity
        else:
            raise ValueError (f"Недостаточно товара на складе. Запрошено: {quantity}, доступно: {self.quantity}")

        """
        TODO реализуйте метод покупки
            Проверьте количество продукта используя метод check_quantity
            Если продуктов не хватает, то выбросите исключение ValueError
        """

    def __hash__(self):
        return hash(self.name + self.description)

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

    def add_product(self, product: Product, buy_count=1) ->None:
        if self.products.get(product):  # если продукт есть в корзине
            self.products[product] += buy_count #то мы добавляем товар
        else:
            self.products[product] = buy_count #добавляем новую запись в словать

        """
        Метод добавления продукта в корзину.
        Если продукт уже есть в корзине, то увеличиваем количество
        """

    def remove_product(self, product: Product, remove_count=None):
        """
        Метод удаления продукта из корзины.
        Если remove_count не передан, то удаляется вся позиция
        Если remove_count больше, чем количество продуктов в позиции, то удаляется вся позиция
        """
        if remove_count is None:
            del self.products[product]
        else:
            self.products[product] -= remove_count

    def clear(self): #очистить всю корзину
        self.products = {}


    def get_total_price(self) -> float: #можешь посчитать цену всех товаров в корзине
        total_price = 0 #изначальный итог 0
        for product, quantity in self.products.items(): #для каждого продукта из словаря
            total_price += product.price * quantity  #складывается цену продуктов, записывая в переменную total_price
        return total_price


    def buy(self): #можем купить все товары в корзине
        """
        Метод покупки.
        Учтите, что товаров может не хватать на складе.
        В этом случае нужно выбросить исключение ValueError
        """
        for product, quantity in self.products.items():
            if product.quantity < quantity:
                raise ValueError("Такого кол-во товара нет в наличии")

        for product, quantity in self.products.items():
            product.buy(quantity)

        self.products.clear()
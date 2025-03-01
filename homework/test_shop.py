"""
Протестируйте классы из модуля homework/models.py
"""
from tkinter.font import names

import pytest

from homework.models import Product, QUANTITY_OF_REQUESTED_PRODUCTS, Cart


@pytest.fixture
def product(): #сам продукт
    return Product("book", 100, "This is a book", 1000)

@pytest.fixture
def product2(): #сам продукт
    return Product("Milk", 50, "This is a book", 100)

@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product): #проверяем кол-во
        assert product.check_quantity(QUANTITY_OF_REQUESTED_PRODUCTS)
        # TODO напишите проверки на метод check_quantity
        #pass

    def test_product_buy(self, product): #пытаемся купить продукт
        in_stock = product.quantity
        product.buy(QUANTITY_OF_REQUESTED_PRODUCTS)
        assert product.quantity == in_stock - QUANTITY_OF_REQUESTED_PRODUCTS
        print(product.quantity)
        print(in_stock - QUANTITY_OF_REQUESTED_PRODUCTS)
        # TODO напишите проверки на метод buy
        #pass

    def test_product_buy_more_than_available (self, product): #пытаемся купить больше, чем доступно
        with pytest.raises(ValueError):
            product.buy(3000)
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        pass


class TestCart: #тест корзины

    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product(self, product, cart):
        count_of_first = 10
        cart.add_product(product=product, buy_count=count_of_first) #к словарю применяем функцию
        assert cart.products[product] == count_of_first #если ранее такого key не было, добавляем запись и сверяем c ранее запрошенным
        count_of_second = 5
        cart.add_product(product=product, buy_count=count_of_second) #повторяем процедуру
        assert cart.products[product] == count_of_first + count_of_second #получается, что в данным момент не создаем, а добавляем к текущему значению

    def test_remove_product(self, cart, product): # удаление продукта из корзины
        add_count = 10
        cart.add_product(product, buy_count=add_count)
        cart.remove_product(product, remove_count=2)
        assert cart.products[product] == 8

    def test_clear(self, cart, product): # очистить всю корзину
        cart.clear()
        assert cart.products == {}

    def test_get_total_price(self, cart, product, product2): # посчитать цену всех товаров в корзине
        quantity1 = 10  # Количество первого продукта
        quantity2 = 20  # Количество второго продукта
        #add_count_milk = 2
        cart.add_product(product, buy_count=quantity1)
        cart.add_product(product2, buy_count=quantity2)

        assert cart.get_total_price() == 2000 # общая цена: (100 * 10) + (50 * 20) = 1000 + 1000 = 2000

    def test_buy(self, cart, product,  product2): # купить все товары в корзине
        quantity1 = 10  # Количество первого продукта
        quantity2 = 20  # Количество второго продукта
        # add_count_milk = 2
        cart.add_product(product, buy_count=quantity1)
        cart.add_product(product2, buy_count=quantity2)
        cart.buy()
        assert product.quantity == 990 #остатки стока
        assert product2.quantity == 80 #остатки стока
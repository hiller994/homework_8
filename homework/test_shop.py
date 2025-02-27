"""
Протестируйте классы из модуля homework/models.py
"""
from tkinter.font import names

import pytest

from homework.models import Product, QUANTITY_OF_REQUESTED_PRODUCTS


@pytest.fixture
def product(): #сам продукт
    return Product("book", 100, "This is a book", 1000)


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product): #проверяем кол-во
        assert product.check_quantity(QUANTITY_OF_REQUESTED_PRODUCTS)
        #Как вывести отрицательный результат? что
        # TODO напишите проверки на метод check_quantity
        #pass

    def test_product_buy(self, product): #пытаемся купить продукт
        # TODO напишите проверки на метод buy
        pass

    def test_product_buy_more_than_available (self, product): #пытаемся купить больше, чем доступно
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
QUANTITY_OF_REQUESTED_PRODUCTS = 800
import pytest

from homework.models import Product, Cart


@pytest.fixture
def product(): #сам продукт
    return Product("book", 100, "This is a book", 1000)

@pytest.fixture
def product2(): #сам продукт
    return Product("Milk", 50, "This is a Milk", 100)

@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    def test_product_check_quantity(self, product): # проверяем кол-во
        assert product.check_quantity(product.quantity - 1) is True
        assert product.check_quantity(product.quantity) is True
        assert product.check_quantity(product.quantity + 1) is False


    def test_product_buy(self, product): #пытаемся купить продукт
        in_stock = product.quantity
        product.buy(QUANTITY_OF_REQUESTED_PRODUCTS)
        assert product.quantity == in_stock - QUANTITY_OF_REQUESTED_PRODUCTS

    def test_product_buy_more_than_available (self, product): # пытаемся купить больше, чем доступно
        with pytest.raises(ValueError):
            product.buy(product.quantity + 1)


class TestCart: # тест корзины
    def test_add_product(self, product, cart):
        count_of_first = 10
        cart.add_product(product=product, buy_count=count_of_first) #к словарю применяем функцию
        assert cart.products[product] == count_of_first #если ранее такого key не было, добавляем запись и сверяем c ранее запрошенным
        count_of_second = 5
        cart.add_product(product=product, buy_count=count_of_second) #повторяем процедуру
        assert cart.products[product] == count_of_first + count_of_second #получается, что в данным момент не создаем, а добавляем к текущему значению

    def test_remove_product(self, cart, product): # удаление продукта из корзины
        # удалили частично (добавили 3, удалили 2)
        add_count = 3
        cart.add_product(product, buy_count=add_count)
        cart.remove_product(product, remove_count=2)
        assert cart.products[product] == 1

    def test_remove_product2(self, cart, product, product2):
        # удалили частично (добавили несколько товаров и удаляем только 1 тип)
        add_count = 3
        cart.add_product(product, buy_count=add_count)
        cart.add_product(product2, buy_count=add_count)
        cart.remove_product(product2, remove_count=3)
        assert cart.products[product] == 3
        assert product2 not in cart.products

    def test_remove_product3(self, cart, product):
        # удалили без количества (добавили 3, удалили)
        add_count = 3
        cart.add_product(product, buy_count=add_count)
        cart.clear()
        assert product not in cart.products

    def test_remove_product4(self, cart, product):
        # удалили больше чем было (добавили 3, пробуем удалить 4)
        add_count = 3
        cart.add_product(product, buy_count=add_count)
        cart.remove_product(product, remove_count=4)
        assert product not in cart.products

    def test_clear(self, cart, product): # очистить всю корзину
        cart.clear()
        assert cart.products == {}

    def test_get_total_price(self, cart, product, product2): # посчитать цену всех товаров в корзине
        quantity1 = 10  # Количество первого продукта
        quantity2 = 20  # Количество второго продукта
        cart.add_product(product, buy_count=quantity1)
        cart.add_product(product2, buy_count=quantity2)
        assert cart.get_total_price() == 2000 # общая цена, пересчитать руками (100 * 10) + (50 * 20) = 1000 + 1000 = 2000

    def test_buy(self, cart, product,  product2): # купить все товары в корзине
        quantity1 = 10  # Количество первого продукта
        quantity2 = 20  # Количество второго продукта
        cart.add_product(product, buy_count=quantity1)
        cart.add_product(product2, buy_count=quantity2)
        cart.buy()
        assert product.quantity == 990 #остатки стока1
        assert product2.quantity == 80 #остатки стока2

    # случай, когда добавили пару разных продуктов, но не хватает одного из них
    def test_buy2(self, cart, product,  product2):
        quantity1 = 10  # Количество первого продукта
        quantity2 = 101  # Количество второго продукта (но на складе 100)
        cart.add_product(product, buy_count=quantity1)
        cart.add_product(product2, buy_count=quantity2)
        with pytest.raises(ValueError) as exc_info:
            cart.buy()
        assert str(exc_info.value) == f"Недостаточно товара: {product2.name} Запрошено: {quantity2}, доступно: {product2.quantity}"
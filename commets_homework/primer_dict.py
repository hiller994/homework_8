'''
import pytest

from homework.models import Product


@pytest.fixture
def product(): #сам продукт
    return Product("book", 100, "This is a book", 1000)
'''

#Cart= {} # у нас есть пустой словарь
Cart= {"Ключ" : 3}
def add_in_dict():
    if "Ключ" in Cart:
        Cart["Ключ"] += 1 #если у нас есть ключ в словаре, то мы добавляем + 1 к значению
    else: # в противном случае мы создаем запись
        Cart["Ключ"] = 3 #добавляем ключ и нужное значение значение в словаре
    print(Cart)
'''
def new_add():
    add_in_dict()
    if "Ключ" in Cart:
        Cart["Ключ"] += 1
    print(Cart)
'''
#вызов функции
add_in_dict()
#new_add()

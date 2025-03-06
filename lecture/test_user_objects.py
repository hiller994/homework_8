#применяем объектный подход (классы)

#--------------------------------------------------------
# Используем объектный подход работы с данными
#--------------------------------------------------------

#userы это некоторая класс, некоторая абстракция, эти абстракции можем реализовать через классы
#созданим класс users и положем его в дерикторию models

import csv

import pytest

from models.providers import UserProvider, CsvUserProvider
from models.users import User, USERS_ADULT_AGE, Status, Worker


#@pytest.fixture
#def users(): #откываем файл (добавляем типизацию ниже. синтаксис типизации "-> list[User]")

'''
def users() -> list[User]: # теперь фикстура Users будет возращать список пользователей
    with open("users.csv") as f:
        users = list(csv.DictReader(f, delimiter=";")) #мы читаем всё, что лежит в csv с помощью DictReader (делает данные читаемыми в виде словаря)
    #return users
    return [
        User(name=user["name"],
             age=int(user["age"]),
             #status=user["status"],
             status=Status(user["status"]),
             items=user["items"])
        for user in users
    ] #на каждую итерацию данного цикла мы создаем экземпляр класса юзер
'''
#Теперь воспользуемся классом провайдера для открытие файла
@pytest.fixture
def user_provider() -> UserProvider: #это будет функция, которая вернет UserProvider
    return CsvUserProvider() #rkfcc функцию по открытию csv

@pytest.fixture
def users(user_provider) -> list[User]:
    return user_provider.get_users()


#далее коммент относится к классу в файле users.py
#теперь тут возвращается нет список словарей users = list(csv.DictReader(f, delimiter=";")), а возврщать список моделей (из класса?)

@pytest.fixture
#def workers(users) -> list[User]:
def workers(users) -> list[Worker]: #после добавления воркера
    '''
    Берем только работников из списока пользователей
    '''
    #workers = [user for user in users if user["status"] == "worker"]  # -- для каждого пользователя(user) в списке пользователей (users), если статус этого пользователя(user) == "worker", просто возьми его и положи в результирующий список
    #теперь будет user.status == "worker" (ЭТО ПОСЛЕ ДОБАВЛЕНИЯ КЛАССА)
    #workers = [user for user in users if user.status == "worker"]
    #ПЕРЕДЕЛЫВАЕМ, ТАК КАК ДОБАВИЛИ КЛАСС ПО ВОЗРАСТУ
    #workers = [user for user in users if user.status == Status.worker]

    #После добавления класса Worker
    workers = [Worker(name=user.name, age=user.age, items=user.items) for user in users if user.status == Status.worker]

    return workers

def test_workers_are_adults_v2(workers):
    '''
    Тестируем, что все работники старше 18 лет
    '''
    for worker in workers:
        assert int(worker["age"]) >= 18, f"Worler {worker['name']} младше 18 лет"  # конвертируем наш возраст, т.к. данные из файла приходят в виде строки


def test_workers_are_adults_v3(workers):
    for worker in workers:
        #assert user_is_adult(worker), f"Worler {worker['name']} младше 18 лет"
        #после добавления класса теперь пишем worker.name
        #assert user_is_adult(worker), f"Worler {worker.name} младше 18 лет"
        #ИЛИ
        #assert worker.age >= USERS_ADULT_AGE, f"Worler {worker.name} младше {USERS_ADULT_AGE} лет"

        #ПОСЛЕ ДОБАВЛЕНИЯ ФУНКЦИ ПО ПРОВЕРКЕ ВОЗРАСТА, после точки просто указываем функцию:
        assert worker.is_adult(), f"Worler {worker.name} младше {USERS_ADULT_AGE} лет"
        #если же нужно проверить обратное, то пишем assert not

'''
#def user_is_adult(user):
def user_is_adult(user: User): #Показываем, что функция принимает на вход экземпляр класса юзер
    #return int(user["age"]) >=18
    # после добавления класса теперь пишем user.age
    return user.age >= 18
'''
#улучшение теста из файла test_users_simple.py, путем добавления фикстур
import csv

import pytest


@pytest.fixture
def users(): #откываем файл
    with open("users.csv") as f:
        users = list(csv.DictReader(f, delimiter=";")) #мы читаем всё, что лежит в csv с помощью DictReader (делает данные читаемыми в виде словаря)
    return users


@pytest.fixture
def workers(users):
    '''
    Берем только работников из списока пользователей
    '''
    workers = [user for user in users if user["status"] == "worker"]  # -- для каждого пользователя(user) в списке пользователей (users), если статус этого пользователя(user) == "worker", просто возьми его и положи в результирующий список
    return workers

def test_workers_are_adults_v2(workers):
    '''
    Тестируем, что все работники старше 18 лет
    '''
    for worker in workers:
        assert int(worker["age"]) >= 18, f"Worler {worker['name']} младше 18 лет"  # конвертируем наш возраст, т.к. данные из файла приходят в виде строки


#Пример, где выносим число 18

'''
def test_workers_are_adults_v2(workers):
    for worker in workers:
        assert user_is_adult(worker), f"Worler {worker['name']} младше 18 лет"

def user_is_adult(user):
    rutern int(user["age"]) >=18
'''

#ДЛЯ ЕЩЕ КРУТОГО УЛУЧЕШЕНИЯ ЧИТАЕМОСТИ КОДА ДОБАВИМ КЛАССЫ test_user_objects.py

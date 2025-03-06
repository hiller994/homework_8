#Полиморфизм
import csv

from lecture.models.users import User, Status


#создание класса для получения данных
# в классе опишем как мы будем получать пользователя с помощью данного провайдера

class UserProvider:
    def get_users(self) -> list[User]: #на выходе должна дать лист моделек User
        raise NotImplementedError #при попытке вызвать фнуцию просто так будет вызвано исключение, т.е. эта функция не реализована в данный момент
        #далее будут другие классы, которые ее реализуют


class CsvUserProvider(UserProvider):
    def get_users(self) -> list[User]:
        with open("users.csv") as f:
            users = list(csv.DictReader(f, delimiter=";"))  # мы читаем всё, что лежит в csv с помощью DictReader (делает данные читаемыми в виде словаря)
        # return users
        return [
            User(name=user["name"],
                 age=int(user["age"]),
                 # status=user["status"],
                 status=Status(user["status"]),
                 items=user["items"])
            for user in users
        ]

#Теперь вызовем этот класс в тесте









class DatabaseUserProvider(UserProvider):
    def get_users(self) -> list[User]:
        pass

class ApiUserProvider(UserProvider):
    def get_users(self) -> list[User]:
        pass


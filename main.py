# from math import pi
# import decimal
#
#
# class Circle:
#     def __init__(self, radius: float):
#         self.radius: float = radius
#         self.__circle_long: (decimal, None) = None
#         self.__area: (decimal, None) = None
#
#     @property
#     def radius(self):
#         return self._radius
#
#     @radius.setter
#     def radius(self, radius: float):
#         self._radius = radius
#
#     @property
#     def circle_long(self) -> decimal:
#         if self.__circle_long is None:
#             self.__circle_long = decimal.Decimal(pi * self.radius * 2)
#         return self.__circle_long
#
#     @property
#     def area(self) -> decimal:
#         if self.__area is None:
#             self.__area = decimal.Decimal(pi * pow(self.radius, 2))
#         return self.__area
#
#
# if __name__ == '__main__':
#     new_circle = Circle(12)
#     print(new_circle.circle_long)
# #     print(new_circle.area)
# 📌Создайте класс прямоугольник. 📌Класс должен принимать длину и ширину при создании экземпляра. 📌У класса должно быть два метода, возвращающие периметр и площадь. 📌Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.
import random
#
#
# class Square:
#     def __init__(self,lenght,width = None):
#         self.length = lenght
#         if width:
#             self.widht = width
#         else:
#             self.widht = lenght
#
#     def square(self):
#             return self.length * self.length
#
#     def perimetr(self):
#         return  (self.length * self.length) * 2
#
# square1 = Square(2)
#
# print(square1.square())
# print(square1.perimetr())
#
# 📌Напишите класс для хранения информации о человеке: ФИО, возраст и т.п. на ваш выбор. 📌У класса должны быть методы birthday для увеличения возраста на год, full_name для вывода полного ФИО и т.п. на ваш выбор. 📌Убедитесь, что свойство возраст недоступно для прямого изменения, но есть возможность получить текущий возраст.
#
#
# class Person:
#     def __init__(self,first_name,second_name,last_name,phone,age):
#         self.first_name =first_name
#         self.second_name = second_name
#         self.last_name = last_name
#         self.age = age
#         self.phone = phone
#
#
#     def birthday(self):
#         self._age += 1
#     def full_name(self):
#         return f'{self.last_name} {self.first_name} {self.second_name}'
#     def person_age(self):
#         return  self.person_age()
#
#     p1 = Person("Илья","Петрович","Иванов", 12445,32)
#     print(p1.person_age())
#     p1.birthday()
#     print(p1.person_age())
#     print(p1.full_name())
# 📌Создайте класс Сотрудник. 📌Воспользуйтесь классом человека из прошлого задания. 📌У сотрудника должен быть: ○шестизначный идентификационный номер ○уровень доступа вычисляемый как остаток от деления суммы цифр id на семь


#
class Animal:
    def __init__(self, name:str=None, breed:str='unknown', age: int = 0):
        self.name = name
        self.breed = breed
        self.age = age

    def print_specific(self):
        return f'Специфические данные'

class Dog(Animal):
    def __init__(self, name:str=None, breed:str='unknown', commands: list[str] = 'unknown'):
        super().__init__(name, breed)
        # self.name = name
        # self.breed = breed
        self.commands = commands

    def print_specific(self):
        return f'{self.commands}'

class Fish(Animal):
    def __init__(self, name: str = None, breed: str = 'unknown', count_fins: int = 0):
        super().__init__(name, breed)
        # self.name = name
        # self.breed = breed
        self.count_fins = count_fins

    def print_specific(self):
        return f'{self.count_fins}'

class Bird(Animal):
    def __init__(self, name: str = None, breed: str = 'unknown', count_flights: int = 0):
        super().__init__(name, breed)
        # self.name = name
        # self.breed = breed
        self.count_flights = count_flights

    def print_specific(self):
        return f'{self.count_flights}'




if __name__ == '__main__':
    dog = Dog('Kat', 'Husky', ['Голос', 'Сидеть'])
    fish = Fish('Nemo', 'Gold Fish', 3)
    bird = Bird('Kesha', 'Попугай', 2)
    animal = Animal('Lexa', 'Cat', 12)
    print(animal.print_specific())
    print(dog.print_specific())
    print(fish.print_specific())
    print(bird.print_specific())


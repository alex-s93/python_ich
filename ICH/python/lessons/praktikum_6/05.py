# Создать класс Person и несколько объектов данного класса. При создании
# объектов данного класса должны прокидываться обязательные атрибуты: рост,
# вес, год рождения и пол. Пол может быть только либо мужской либо женский.
# Дополнить класс Person операцией сложения. При сложении двух объектов этого
# класса (обязательно разнополых) операция должна возвращать новый объект
# класса Person, у которого рост - четверть от среднего арифметического роста
# родителей, вес - двадцатая часть от среднего арифметического веса родителей,
# год рождения - текущий, значение пола случайное или мужчина или женщина.
# Дополнительно придумать и определить методы _len_, _bool_.
from enum import Enum
from datetime import datetime
import random


class Gender(Enum):
    male = "Male"
    female = "Female"


class Person:
    def __init__(self, height: float, weight: float, birthday: str, gender: Gender):
        self.height = height
        self.weight = weight
        self.birthday = datetime.strptime(birthday, "%Y-%m-%d")
        self.gender = gender

    def __add__(self, other):
        if self.gender != other.gender:
            height = (self.height + other.height)/8
            weight = (self.weight + other.weight)/40
            birthday = str(datetime.today().date())
            gender = random.choice(list(Gender))
            return Person(height, weight, birthday, gender)

    def __str__(self):
        return f"Person(Height: {self.height}, Weight: {self.weight}, Birthday: {self.birthday}, Gender: {self.gender.value})"

    def __len__(self):
        # вычисляем какой длины отрезок жизни человек уже прожил (количество полных лет xD)
        if self.birthday.date() == datetime.today().date():
            return 0

        return int(str(datetime.today().date() - self.birthday.date()).split(' day')[0])//365

    def __bool__(self):
        # проверяем на совершеннолетие
        return len(self) > 18


if __name__ == "__main__":
    person_1 = Person(1.70, 75.5, "1990-12-11", Gender.male)
    person_2 = Person(1.80, 81.2, "1999-11-12", Gender.female)

    person_3 = person_1 + person_2

    print(person_3)
    print(len(person_2))
    print(bool(person_2))
    print(bool(person_3))


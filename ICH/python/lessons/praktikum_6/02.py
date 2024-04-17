from datetime import datetime


class Person:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = datetime.strptime(birthday, "%Y-%m-%d")

    def get_age(self):
        # (datetime.today().date() - datetime.strptime("1990-07-13", "%Y-%m-%d").date()).days/365
        return int(str((datetime.today().date() - self.birthday.date()) / 365).split('days')[0])


class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

    def __repr__(self):
        return f"({self})"


if __name__ == '__main__':
    p1 = Person("Alex", "1990-07-13")
    p2 = Person("Billy", "1994-01-10")
    p3 = Person("Garet", "2015-05-03")
    p4 = Person("Lily", "2014-04-09")
    p5 = Person("Jimmy", "1967-02-26")
    p6 = Person("Luka", "2001-09-21")
    p7 = Person("Sandy", "1978-10-11")
    p8 = Person("Sidney", "1999-01-29")
    p9 = Person("Bart", "1993-12-02")
    p10 = Person("Dreik", "1980-02-01")

    persons = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]

    employees = [Employee(person.name, person.get_age()) for person in persons if person.get_age() > 18]

    print(employees)

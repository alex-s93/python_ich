# 2. Создайте класс Student для представления студента. Класс должен иметь атрибуты name (имя) и age (возраст),
# а также метод display_info(), который выводит информацию о студенте. Затем создайте экземпляр класса Student с
# заданным именем и возрастом и вызовите метод display_info().

class Student:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_info(self):
        return f'{self.name}, {self.age}'


student = Student('John', 32)

print(student.get_info())

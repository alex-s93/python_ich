# 1. Создайте класс Rectangle для представления прямоугольника.
# Класс должен иметь атрибуты width (ширина) и height (высота), а также метод calculate_area(), который вычисляет
# площадь прямоугольника. Затем создайте экземпляр класса Rectangle с заданными значениями ширины и высоты и выведите
# его площадь.


# NOTE: Так как не было указано каким именно способом мы должны устанавливать значения в классе -
# было реализовано два класса с разными способами. И было создано две модели, реализующие разные классы.

class Rectangle:
    def __init__(self, width: int | float, height: int | float):
        self.width = width
        self.height = height

    def calculate_area(self) -> int | float:
        return self.width * self.height


class Rectangle2:
    width: int | float = None
    height: int | float = None

    def calculate_area(self) -> int | float:
        return self.width * self.height


rectangle_1 = Rectangle(11.5, 10)

rectangle_2 = Rectangle2()
rectangle_2.width = 15
rectangle_2.height = 9

print("The area of first rectangle is:", rectangle_1.calculate_area())
print("The area of second rectangle is:", rectangle_2.calculate_area())

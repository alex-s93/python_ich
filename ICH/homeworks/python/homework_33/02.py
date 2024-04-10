# 2. Реализуйте абстрактный базовый класс Shape (фигура), а от него унаследуйте классы Rectangle (прямоугольник) и
# Circle (круг). Класс Shape должен иметь абстрактный метод area, который должен быть реализован в каждом дочернем
# классе. Классы Rectangle и Circle также должны иметь метод perimeter для расчета периметра. Выведите площадь и
# периметр прямоугольника и круга на экран.
#
#
# Пример использования:
#
# rectangle = Rectangle(5, 3)
# circle = Circle(2)
#
# print(f"Rectangle area: {rectangle.area()}")  # Вывод: Rectangle area: 15
# print(f"Rectangle perimeter: {rectangle.perimeter()}")  # Вывод: Rectangle perimeter: 16
# print(f"Circle area: {circle.area()}")  # Вывод: Circle area: 12.566370614359172
# print(f"Circle perimeter: {circle.perimeter()}")  # Вывод: Circle perimeter: 12.566370614359172
import math
from abc import ABC, abstractmethod


class AbstractShape(ABC):
    @abstractmethod
    def area(self):
        raise NotImplementedError

    @abstractmethod
    def perimeter(self):
        raise NotImplementedError


class Rectangle(AbstractShape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(AbstractShape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


if __name__ == '__main__':
    rectangle = Rectangle(5, 3)
    circle = Circle(2)

    print(f"Rectangle area: {rectangle.area()}")
    print(f"Rectangle perimeter: {rectangle.perimeter()}")
    print(f"Circle area: {circle.area()}")
    print(f"Circle perimeter: {circle.perimeter()}")

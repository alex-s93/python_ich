# 1. Создайте класс Rectangle для представления прямоугольника.
# Класс должен иметь атрибуты width (ширина) и height (высота) со значениями по умолчанию,
# а также методы calculate_area() для вычисления площади прямоугольника и calculate_perimeter() для вычисления периметра
# прямоугольника.
# Переопределить методы __str__, __repr__.
# Затем создайте экземпляр класса Rectangle и выведите информацию о нем, его площадь и периметр.

class Rectangle:
    def __init__(self, width: [int | float] = 0, height: [int | float] = 0):
        self.__width = width
        self.__height = height

    def calculate_area(self) -> int | float:
        return self.__width * self.__height

    def calculate_perimeter(self) -> int | float:
        return 2 * (self.__width + self.__height)

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(width: {self.__width}, height: {self.__height})"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__width}, {self.__height})"


if __name__ == "__main__":
    rectangle_1 = Rectangle(10, 5)
    rectangle_2 = Rectangle()
    rectangle_3 = Rectangle(height=9, width=14)

    for rectangle in (rectangle_1, rectangle_2, rectangle_3):
        print("Info:", rectangle)
        print("Use the next construction for creating the same object:", repr(rectangle))
        print("The area of rectangle is:", rectangle.calculate_area())
        print("The perimeter of rectangle is:", rectangle.calculate_perimeter())
        print("-" * 50)

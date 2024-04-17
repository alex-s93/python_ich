import math


class Shape:
    def __init__(self, name):
        self.name = name

    def calculate_area(self):
        pass

    def __str__(self):
        return f"Name: {self.name}, Area: {self.calculate_area()}"

    def __repr__(self):
        return f"({self})"


class Circle(Shape):
    def __init__(self, radius, name="Circle"):
        super().__init__(name)
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)


class Square(Shape):
    def __init__(self, side, name="Square"):
        super().__init__(name)
        self.side = side

    def calculate_area(self):
        return self.side ** 2


class Rectangle(Shape):
    def __init__(self, width, height, name="Rectangle"):
        super().__init__(name)
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


if __name__ == "__main__":
    circle = Circle(10)
    square = Square(12)
    rectangle = Rectangle(5, 4)

    shapes = [circle, square, rectangle]

    print(list(shapes))

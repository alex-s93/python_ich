import math


class Point:
    DEFAULT_COLOR = 'black'

    def __init__(self, x=0, y=0, color='black'):
        self.x = x
        self.y = y
        self.__color = color

    def get_color(self):
        return self.__color

    def get_distance_to_center(self):
        return round(math.hypot(self.x, self.y), 2)

    def __str__(self):
        return f'Point(x: {self.x}, y: {self.y}, color: {self.__color})'


point_1 = Point()
point_2 = Point(10, 15)
point_3 = Point(y=10, color='red')

# print(point_2.x)
# print(point_2.get_color())
# print(point_2.get_distance_to_center())
print(point_3)

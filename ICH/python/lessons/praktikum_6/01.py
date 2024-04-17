class Car:
    def __init__(self, model, year, color='black'):
        self.__model = model
        self.__year = year
        self.__color = color

    def get_color(self):
        return self.__color

    def __str__(self):
        return f'Model: {self.__model}, Year: {self.__year}, Color: {self.__color}'

    def __repr__(self):
        return f"({self})"


def find_cars_by_color(collection, color):
    return filter(lambda car: car.get_color() == color, collection)


if __name__ == '__main__':
    car1 = Car('Ford', '2013', 'white')
    car2 = Car('VW', '2019', 'red')
    car3 = Car('Mercedes', '2009', 'yellow')
    car4 = Car('Hyundai', '1998', 'blue')
    car5 = Car('Audi', '2020', 'white')
    car6 = Car('Chevrolet', '2001')
    car7 = Car('Kia', '2005', 'orange')
    car8 = Car('Maserati', '2021', 'grey')
    car9 = Car('Fiat', '1995', 'green')
    car10 = Car('Nissan', '2005', 'dark-blue')

    cars = [car1, car2, car3, car4, car5, car6, car7, car8, car9, car10]

    filtered_cars = find_cars_by_color(cars, "white")

    print(list(filtered_cars))

# 1. Реализовать класс Counter, который представляет счетчик. Класс должен поддерживать следующие операции:
# - Увеличение значения счетчика на заданное число (оператор +=)
# - Уменьшение значения счетчика на заданное число (оператор -=)
# - Преобразование счетчика в строку (метод __str__)
# - Получение текущего значения счетчика (метод __int__)
#
# Пример использования:
#
# counter = Counter(5)
#
# counter += 3
# print(counter)  # Вывод: 8
# counter -= 2
# print(int(counter))  # Вывод: 6

class Counter:
    def __init__(self, value):
        self.__value = value

    def __iadd__(self, other):
        self.__value = self.__value + other
        return self.__value

    def __isub__(self, other):
        self.__value = self.__value - other
        return self.__value

    def __str__(self):
        return f"{self.__value}"

    def __int__(self):
        return self.__value


if __name__ == '__main__':
    counter = Counter(5)

    counter += int(3)
    print(counter)  # Вывод: 8
    counter -= 2
    print(counter)  # Вывод: 8

    print(int(counter))  # Вывод: 6

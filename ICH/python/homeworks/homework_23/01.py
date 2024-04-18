# 1. Напишите программу, которая генерирует и выводит квадраты чисел от 1 до N с использованием генераторного выражения.
# Реализуйте функцию generate_squares, которая принимает число N в качестве аргумента и использует генераторное
# выражение для генерации квадратов чисел. Затем выведите квадраты чисел на экран.
# Пример работы программы:
#
# 1
# 4
# 9
# 16
# 25

def generate_squares(number):
    for i in range(1, number + 1):
        yield i ** 2


gen = generate_squares(5)

for i in gen:
    print(i)
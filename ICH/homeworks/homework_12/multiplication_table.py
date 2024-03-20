# 1. Напишите программу, которая запрашивает у пользователя число N и выводит на экран таблицу умножения от 1 до N. Используйте вложенный цикл for для создания таблицы умножения. Выведите результат на экран с помощью команды print.
#
#
# Пример вывода:
#
#
# Введите число N: 5
#

rate = int(input("Enter the number for multiplication: "))

for item in range(1, rate + 1):
    for i in range(1, rate + 1):
        if i != rate:
            print(f"{i * item:^4}", end=" | ")
        else:
            print(i * item)



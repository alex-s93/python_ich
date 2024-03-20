# 2. Напишите программу, которая принимает два списка одинаковой длины и создает новый список, содержащий пары элементов из исходных списков. Используйте функцию zip() для создания пар элементов. Выведите результат на экран с помощью команды print.
#
#
# Пример вывода:
#
#
# Введите элементы первого списка, разделенные пробелом: 1 2 3 4 5
#
# Введите элементы второго списка, разделенные пробелом: A B C D E
#
#
# Список пар элементов: [(1, 'A'), (2, 'B'), (3, 'C'), (4, 'D'), (5, 'E')]

string_1 = input("Enter elements of the first list, separated by whitespace: ")
string_2 = input("Enter elements of the second list, separated by whitespace: ")

for value_1, value_2 in zip(string_1, string_2):
    if value_1 != " " and value_2 != " ":
        print(f"({value_1}, '{value_2}')", end=", ")


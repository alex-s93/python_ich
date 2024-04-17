# 2. Напишите программу, которая принимает произвольное количество аргументов от пользователя и передает их в функцию calculate_sum, которая возвращает сумму всех аргументов. Используйте оператор * при передаче аргументов в функцию. Выведите результат на экран.
# Пример вывода:
#
# Введите числа, разделенные пробелами: 1 2 3 4 5
#
# Сумма чисел: 15
def calculate_sum(*nums):
    return sum(nums)


string = input("Enter numbers separated by whitespace: ")
numbers = (int(i) for i in string.split())

print("The sum of numbers is:", calculate_sum(*numbers))

#1. Напишите программу, которая принимает два числа и возвращает их сумму и произведение в виде кортежа (sum, product).
# Используйте функцию для вычисления суммы и произведения. Выведите результат на экран с помощью команды print.
# Пример вывода:
#
# Введите первое число: 3
#
# Введите второе число: 4
#
# Сумма и произведение чисел: (7, 12)
def sum_product(num_1, num_2):
    summa = num_1 + num_2
    production = num_1 * num_2
    return (summa, production)


num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))

print("Summa and production of numbers is:", sum_product(num_1, num_2))




# 1. Напишите генератор, который будет принимать на вход числа и возвращать их сумму. Генератор должен использовать
# инструкцию yield для возврата текущей суммы и должен продолжать принимать новые числа для добавления к сумме.
# Если генератор получает на вход число 0, он должен прекращать работу и вернуть окончательную сумму. Напишите
# программу, которая будет использовать этот генератор для пошагового расчета суммы чисел, вводимых пользователем.
# Пример вывода:
#
# Введите числа для суммирования (0 для окончания):
# Введите число: 3
# Текущая сумма: 3
# Введите число: 5
# Текущая сумма: 8
# Введите число: 2
# Текущая сумма: 10
# Введите число: 0
# Текущая сумма: 10

def sum_generator():
    summa = 0
    try:
        while True:
            num = yield summa
            if num == 0:
                raise StopIteration(summa)
            summa += num
    except StopIteration:
        return summa


gen = sum_generator()
next(gen)

while True:
    number = int(input("Enter a number for summing (or 0 for program finishing): "))
    try:
        print("The current sum is:", gen.send(number))
    except StopIteration as result:
        print("The current sum is:", result)
        gen.close()
        break

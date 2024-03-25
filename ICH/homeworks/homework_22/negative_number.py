# 1. Напишите программу, которая открывает файл, считывает из него два числа и выполняет операцию их деления.
# Если число отрицательное, выбросите исключение ValueError с сообщением "Число должно быть положительным".
# Обработайте исключение и выведите соответствующее сообщение.

def divide_values(val_1, val_2):
    if val_1 < 0 or val_2 < 0:
        raise ValueError("The numbers cannot be negative.")
    return val_1 / val_2


# NOTE: В файле task_1.txt должно храниться два числа разделенные пробелом
with open("task_1.txt") as file:
    try:
        value_1, value_2 = file.readline().split()
        result = divide_values(int(value_1), int(value_2))
        print("The result of division is: ", result)
    except ValueError as err:
        print(err, "Please, check the numbers in the file.")

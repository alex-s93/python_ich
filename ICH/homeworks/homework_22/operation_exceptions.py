# 2. Напишите программу, которая открывает файл, считывает его содержимое и выполняет операции над числами в файле.
# Обработайте возможные исключения при открытии файла (FileNotFoundError) и при выполнении операций над числами
# (ValueError, ZeroDivisionError). Используйте конструкцию try-except-finally для обработки исключений и закрытия файла
# в блоке finally.

# NOTE: В файле task_2.txt можно записать несколько пар чисел, разделенных запятой. Каждая пара должна быть с новой строчки

try:
    file = open("task_2.txt")
except FileNotFoundError as err:
    print("You have entered not existing path for the file. Please, check yourself.")
else:
    try:
        for line in file.readlines():
            value_1, value_2 = line.replace("\n", "").split(",")
            try:
                print("Numbers for operations:", value_1, value_2)
                print("Sum is:", int(value_1) + int(value_2))
                print("Difference is:", int(value_1) - int(value_2))
                print("Multiplication is:", int(value_1) * int(value_2))
                print("Division is:", int(value_1) / int(value_2))
            except ValueError as err:
                print(f"{value_1} or {value_2} is not a numeric value.", )
            except ZeroDivisionError:
                print("It's forbidden to divide by 0")
            finally:
                print("-" * 50)
    finally:
        file.close()

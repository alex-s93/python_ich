# 8. Напишите программу, которая запрашивает у пользователя имя файла
# (переменная file) и целое число (переменная lines), а затем выводит на экран
# построчно строки в количестве lines (на всякий случай проверим, что задано
# положительное целое число). Протестируем функцию на файле article.txt
# со следующим содержимым:
#
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела

file_name = input("Enter file name: ")

while True:
    lines_numbers = input("Enter how much lines you wanna print: ")
    if not (lines_numbers.isdigit() and int(lines_numbers) > 0):
        print("Invalid entered value. Try again.", end=" ")
        continue
    with open(file_name) as file:
        for i in range(int(lines_numbers)):
            print(file.readline().strip())

    break

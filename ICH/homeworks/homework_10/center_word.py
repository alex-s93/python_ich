# 3. Напишите программу, которая запрашивает у пользователя строку и выравнивает ее по центру с заданной шириной.
# Если строка не может быть выровнена по центру из-за нечетной ширины, она должна быть выровнена смещением вправо.
# Используйте методы center() и rjust() для выравнивания строки.
#
# Пример вывода:
#
# Введите строку: Python
# Введите ширину: 10
# Результат:
#
#   Python


# если пользователь ставит пробелы перед и/или после своего слова/предложения -
# пустые пробелы в начале и конце строки будут убираться с помощью strip()
string = input("Enter a string: ").strip()

width = int(input("Enter a width: "))

if width < len(string):
    print("The width should be more than string's length")
else:
    if len(string) % 2 != width % 2:
        string = string.rjust(len(string) + 1)
    string = string.center(width)
    print(f"'{string}'")

# 2. Напишите программу, которая принимает строку от пользователя и подсчитывает количество уникальных символов в этой
# строке. Создайте функцию count_unique_chars, которая принимает строку и возвращает количество уникальных символов.
# Выведите результат на экран.
#
# Пример вывода:
# Введите строку: hello
#
# Количество уникальных символов: 4

def count_unique_chars(value):
    return len(set(value))


string = input("Enter a string: ")
print("Amount of uniq symbols in the string:", count_unique_chars(string))

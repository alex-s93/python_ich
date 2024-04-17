# 1. Напишите функцию merge_dicts, которая принимает произвольное количество словарей в качестве аргументов и возвращает
# новый словарь, объединяющий все входные словари. Если ключи повторяются, значения должны быть объединены в список.
# Функция должна использовать аргумент **kwargs для принятия произвольного числа аргументов словаря.
# Пример ввода:
#
# {'a': 1, 'b': 2}
#
# {'b': 3, 'c': 4}
#
# {'c': 5, 'd': 6}
#
# Пример вывода:
#
# {'a': [1], 'b': [2, 3], 'c': [4, 5], 'd': [6]}
from ast import literal_eval


def merge_dicts(**dictionaries):
    new_dict = {}
    for item in dictionaries.values():
        for key, value in item.items():
            if key not in new_dict:
                new_dict[key] = [value]
            else:
                new_dict[key].append(value)
    return new_dict


def get_dicts_from_usr():
    dicts = {}
    key = 0

    while True:
        string = input("Enter a dictionary or 'quit' to quit: ")
        if string.lower() == "quit":
            break
        dicts[str(key)] = literal_eval(string)
        key += 1

    return dicts


print(merge_dicts(**get_dicts_from_usr()))

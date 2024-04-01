# Напишите функцию, которая принимает на вход список чисел и возвращает сумму квадратов только четных чисел из списка,
# используя функциональные подходы (например, map, filter и reduce).
#
# Пример вывода:
# Введите числа: 4, 6, 3, 4, 2, 3, 9, 0, 7
#
# Результат: 72

def specific_calculation(collection: list[int]) -> int:
    # even_num_list = filter(lambda x: x % 2 == 0, collection)
    # finish_num_list = map(lambda x: x ** 2, even_num_list)
    # return sum(finish_num_list)
    #
    # NOTE: для читаемости лучше конечно так как выше, но в этот раз решил использовать многочисленную вложенность:)

    return sum(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, collection)))


num_list = [int(x) for x in input("Enter numbers separated by comma: ").split(',')]

print("The result is:", specific_calculation(num_list))

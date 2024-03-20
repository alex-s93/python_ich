# 2. Напишите программу, которая принимает список чисел и возвращает сумму, минимальное и максимальное значение из списка.
# Используйте функцию для обработки списка чисел и возврата трех значений. Выведите результат на экран с помощью команды print.
# Пример вывода:
#
# Введите числа:  3, 7, 2, 9, 1, 5
#
# Сумма чисел: 27
#
# Минимальное значение: 1
#
# Максимальное значение: 9
def convert_to_int_list_sorted(num_list):
    new_list = []
    for item in num_list:
        new_list.append(int(item))
    new_list.sort()
    return new_list


def num_processing(num_list):
    new_list = convert_to_int_list_sorted(num_list)
    min_n = new_list[0]
    max_n = new_list[-1]
    num_sum = 0
    for i in new_list:
        num_sum += int(i)
    return min_n, max_n, num_sum


num_list = input("Enter several numbers separated by a comma: ").split(",")

min_n, max_n, num_sum = num_processing(num_list)
print("Numbers summa: ", num_sum)
print("Minimal value: ", min_n)
print("Maximal value: ", max_n)

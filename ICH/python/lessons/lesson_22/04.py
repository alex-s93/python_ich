# 4. Дан список целых чисел длины 1 и более. Написать функцию, которая возвращает
# список длины 2, состоящий из первого и последнего элемента входного списка.
# [1, 2, 3] -> [1, 3], [7, 4, 6, 2] -> [7, 2], [5] -> [5, 5]
def first_n_last_element(numbers_list):
    return [numbers_list[0], numbers_list[-1]]


num_list = [5]

print(first_n_last_element(num_list))

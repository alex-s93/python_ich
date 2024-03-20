# 1. Напишите программу, которая принимает матрицу (вложенный список) от пользователя и находит сумму всех элементов в матрице. Используйте вложенные списки и циклы для обхода элементов матрицы.
# Пример матрицы: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# Пример вывода:
#
# Сумма элементов в матрице: 45

def convert_string_to_matrix(string):
    init_list = string.split("],")

    # string_list = [i.replace("[", "").replace("]", "").split(",") for i in init_list]
    # final_list = [[int(s) for s in i] for i in string_list]
    # ________________________________________________________________________________________________________________________
    # код выше можно записать в одну строку, но как по мне - ухужшается читаемость. какой вариант лучше - верхний или нижний?

    final_list = [[int(s) for s in i.replace("[", "").replace("]", "").split(",")] for i in init_list]

    return final_list


string = input("Enter a matrix: ")

n_list = convert_string_to_matrix(string)
summa = sum(sum(i) for i in n_list)

print("The sum of all elements in matrix is: ", summa)

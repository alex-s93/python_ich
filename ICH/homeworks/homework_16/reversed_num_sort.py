# 2. Напишите программу, которая принимает список чисел от пользователя и сортирует его в порядке убывания, используя метод sort() и параметр reverse=True. Выведите отсортированный список на экран.

# Пример вывода:

# Введите список чисел, разделенных пробелами: 5 2 8 1 3

# Отсортированный список чисел: [8, 5, 3, 2, 1]

string = input('Enter a several numbers separated by whitespace: ')

num_list = [int(i) for i in string.split()]
num_list.sort(reverse=True)

print("Sorted list in desc order: ", num_list)

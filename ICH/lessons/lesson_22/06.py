# 6. Напишите lamda-функцию, которая вернет количество четных чисел в списке.
# [1, 5, 4, 2, 3, 0] -> 2, [1, 2, 3, 4, 5, 6] -> 3, [1, 5, 7, 11] -> 0

num_list = [1, 5, 4, 2, 3, 0]
# num_list = [1, 2, 3, 4, 5, 6]
# num_list = [1, 5, 7, 11]

# count = 0
#
# for item in num_list:
#     if item % 2 == 0 and item != 0:
#         count += 1
#
# print(count)
num_list = [1, 5, 4, 2, 3, 0]

print((lambda my_list: len([i for i in my_list if i % 2 == 0 and i != 0]))(num_list))

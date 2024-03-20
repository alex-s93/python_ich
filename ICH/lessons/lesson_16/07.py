# 7. Дана строка. Если в этой строке буква f встречается только один раз,
# выведите её индекс. Если она встречается два и более раз, выведите индекс её
# первого и последнего появления. Если буква f в данной строке не встречается,
# ничего не выводите. При решении этой задачи не стоит использовать циклы.

string = input("Enter some text: ")

f_count = string.count("f")

if f_count == 1:
    print(string.index("f"))
elif f_count >= 2:
    print(string.index("f"), string.rindex("f"))
elif f_count == 0:
    pass


#string = input('enter string: ')

# count_1 = None
# count_2 = None
#
# for index, item in enumerate(string):
#     if item.lower() == 'f':
#         if count_1 is None:
#             print('first f', index)
#             count_1 = index
#         else:
#             count_2 = index
#
# if count_2 is not None:
#     print('last f', count_2)
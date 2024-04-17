# 2. Напишите функцию is_subset, которая принимает два множества set1 и set2 и проверяет,
# является ли set1 подмножеством set2. Функция должна возвращать True, если все элементы из set1 содержатся в set2,
# и False в противном случае. Функция должна быть реализована без использования встроенных методов issubset или <=.
#
# Пример множеств
# {1, 2, 3}
# {1, 2, 3, 4, 5}
#
# Пример вывода:
# True

def check_is_subset(set_1, set_2):
    if len(set_1) > len(set_2):
        return ("First set can't be subset of second set, "
                "because the length of first set is more than the length of second set")

    is_subset = True
    for item in set_1:
        if item not in set_2:
            is_subset = False
            break
    return is_subset


first_set = {1, 2, 3}
second_set = {1, 2, 3, 4, 5}

print(check_is_subset(first_set, second_set))

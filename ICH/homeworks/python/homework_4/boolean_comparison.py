# Эта простая функция была создана из-за того, что выражение `bool("False")` возвращает True
def str_to_bool(bool_str):
    if bool_str == "False":
        return False
    else:
        return True


first_bool = str_to_bool(input("Введите первое логическое значение (True или False): "))
second_bool = str_to_bool(input("Введите второе логическое значение (True или False): "))

logic_and = first_bool and second_bool
logic_or = first_bool or second_bool
logic_not_first = not first_bool
logic_not_second = not second_bool
is_equal = first_bool == second_bool
is_not_equal = first_bool != second_bool

print("Результат логического И:", logic_and)
print("Результат логического ИЛИ:", logic_or)
print("Результат логического НЕ (для первого значения):", logic_not_first)
print("Результат логического НЕ (для второго значения):", logic_not_second)
print("Результат сравнения на равенство:", is_equal)
print("Результат сравнения на неравенство:", is_not_equal)

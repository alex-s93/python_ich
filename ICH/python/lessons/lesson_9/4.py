# У нас есть две обезьяны a и b. Они могут улыбаться или не улыбаться (True / False).
# Если они одновременно улыбаются или не улыбаются, то у нас проблемы.
# Написать программу, которaе печатает есть ли у нас проблемы в зависимости
# от улыбчивости обезьян.

is_monkey_a_smiling = eval(input("Is monkey A smiling? (True or False):"))
is_monkey_b_smiling = eval(input("Is monkey B smiling? (True or False):"))

# if (is_monkey_a_smiling and is_monkey_b_smiling) or not (is_monkey_a_smiling or is_monkey_b_smiling):
#     print("Huston, we have a problem!")
# else:
#     print("Everything is OK")

if is_monkey_a_smiling == is_monkey_b_smiling:
    print("Huston, we have a problem!")
else:
    print("Everything is OK")
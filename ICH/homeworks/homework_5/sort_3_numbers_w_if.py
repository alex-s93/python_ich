first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))
third_number = int(input("Введите третье число: "))

min_number = None
middle_number = None
max_number = None

if third_number >= first_number <= second_number:
    min_number = first_number
    if second_number <= third_number:
        middle_number = second_number
        max_number = third_number
    else:
        middle_number = third_number
        max_number = second_number
elif first_number >= third_number <= second_number:
    min_number = third_number
    if first_number <= second_number:
        middle_number = first_number
        max_number = second_number
    else:
        middle_number = second_number
        max_number = first_number
else:
    min_number = second_number
    if first_number <= third_number:
        middle_number = first_number
        max_number = third_number
    else:
        middle_number = third_number
        max_number = first_number

# # defining the biggest number
# if third_number <= first_number >= second_number:
#     max_number = first_number
# elif first_number <= third_number >= second_number:
#     max_number = third_number
# else:
#     max_number = second_number
#
# # set the middle number
# if min_number == first_number:
#     if max_number == second_number:
#         middle_number = third_number
#     else:
#         middle_number = second_number
# elif min_number == second_number:
#     if max_number == first_number:
#         middle_number = third_number
#     else:
#         middle_number = first_number
# else:
#     # here is min_number = third_number
#     if max_number == first_number:
#         middle_number = second_number
#     else:
#         middle_number = first_number

print("Числа в порядке возрастания: ", min_number, middle_number, max_number)


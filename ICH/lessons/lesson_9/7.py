# Вводится вещественное число и нам нужно его округлить до 2 и 3 разряда
# после запятой и вывести полученный результат через пробел в одной строчке.
# Воспользуемся функцией round — встроенная функция Python. Программа должна
# верно округлять как положительные, так и отрицательные числа.

num = float(input("Enter a float number (with several digits after comma): "))

if num >= 0:
    index_2 = 0.001
    index_3 = 0.0001
else:
    index_2 = -0.001
    index_3 = -0.0001

float_2 = round(num + index_2, 2)
float_3 = round(num + index_3, 3)

print("The rounded number is:", float_2, "and", float_3)

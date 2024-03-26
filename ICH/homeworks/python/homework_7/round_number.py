# Напишите программу, принимающую число с плавающей точкой и округляющую его до целого числа в соответствии с
# правилами школьной математики. Использовать модуль math и методы из него нельзя. Учесть, что программа должна
# корректно работать с отрицательными числами.

num = float(input("Enter a float number: "))

int_part = int(num)
float_part = num - int_part

if float_part >= 0.5:
    int_part += 1
elif float_part <= -0.5:
    int_part -= 1

print("The rounded integer is", int_part)

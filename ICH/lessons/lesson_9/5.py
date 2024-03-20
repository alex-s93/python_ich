# Для заданного натурального числа N подсчитать количество четных натуральных
# чисел, меньше или равных N.

num = int(input("Enter the natural number:"))

count = 0

while num > 0:
    if num % 2 == 0:
        count += 1
    num -= 1

print("Amount of even natural numbers before your number (including your number):", count)

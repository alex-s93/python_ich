# Определите среднее значение всех элементов последовательности, завершающейся
# числом 0. Среднее значение - сумма всех элементов, поделенная на их количество.
# Программа запрашивает ввести первое число, потом второе и т.д. до тех пор пока
# не будет введён ноль. Как только вводится ноль программа перестаёт запрашивать
# числа и выводит среднее значение всех введённых до нуля чисел.

summ = 0
count = 0

while True:
    num = int(input("Enter the number:"))
    if num == 0:
        break
    summ += num
    count += 1

avg_num = summ / count

print("The average value of all entered numbers is:", avg_num)
# 2. Даны два целых числа A и B. Напишите функцию, которая печатает все числа
# от A до B включительно или от В до А, если А меньше В.
def print_range(start, stop):
    for i in range(start, stop+1):
        print(i)


num_a = int(input("Enter number A: "))
num_b = int(input("Enter number B: "))

if num_b >= num_a:
    print_range(num_a, num_b)
else:
    print_range(num_b, num_a)


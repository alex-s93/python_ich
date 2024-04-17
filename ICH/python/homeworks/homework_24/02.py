# 2. Напишите генератор, который будет генерировать арифметическую прогрессию

def arithmetic_generator(dif):
    num = 1
    while True:
        yield num
        num += dif


step = int(input("What is step of arithmetic progression? "))
amount = int(input("How many numbers of arithmetic progression would you like to print? "))

gen = arithmetic_generator(step)

for _ in range(amount):
    print(next(gen))

gen.close()

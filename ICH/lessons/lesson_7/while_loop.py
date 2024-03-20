import time
from time import time, sleep

start = time()

number = int(input("Enter a number: "))

result = 1
sleep(1)
while number > 1:
    result *= number
    number -= 1

print(result)


end = time()

print("execution time:", end - start, "second(s)")

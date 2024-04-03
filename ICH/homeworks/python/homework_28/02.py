# Напишите программу, которая принимает список чисел от пользователя и использует функцию reduce из модуля functools,
# чтобы найти произведение всех чисел в списке. Затем программа должна использовать функцию itertools.accumulate для
# накопления произведений чисел в новом списке. В результате программа должна вывести список, содержащий накопленные
# произведения.

from functools import reduce
from itertools import accumulate
from operator import mul

num_list = [int(x) for x in input("Enter some numbers for accumulation separated by comma: ").split(",")]

mul_reduce = reduce(mul, num_list, 1)

mul_accumulate = accumulate(num_list, mul)

print("The result of reduce method:", mul_reduce)
print("The result of accumulation is:", list(mul_accumulate))


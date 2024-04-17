import itertools
import operator
from functools import reduce

numbers = [120, 24, 6, 3, 2, 1]

result = itertools.accumulate(numbers, operator.truediv)
combinations = itertools.zip_longest
print(list(result))

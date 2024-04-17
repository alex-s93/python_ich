from functools import reduce

numbers = [1, 2, 3, 4, 5]
squared_sum = reduce(lambda x, y: x + y ** 2, numbers)

print(squared_sum)

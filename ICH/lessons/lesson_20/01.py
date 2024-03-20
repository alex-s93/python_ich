# ЗАДАЧА: Дан список, нужно вывести сумму квадратов всех элемента списка.
# --------------------------------------------------------------------------------
# пример с джавы:
#
# List<Integer> list = Arrays.asList(1,2,3,4,5,6,7);
# int sum = list.stream().map(x -> x*x).reduce((x,y) -> x + y).get();
# System.out.println(sum);
# --------------------------------------------------------------------------------
# from functools import reduce
#
# num_list = [1, 2, 3, 4, 5, 6, 7]
# summa = reduce(lambda x, y: x + y, list(map(lambda x: x**2, num_list)))
# print(summa)
# --------------------------------------------------------------------------------
# from lazy_streams import stream
#
# num_list = [2, 2, 3, 4, 5, 6, 7]
# summa = (stream(num_list)
#          .map(lambda x: x**2)
#          .reduce(lambda x, y: x+y))
# print(summa)
# --------------------------------------------------------------------------------
from functools import reduce

my_list = [2, 2, 3, 4, 5, 6, 7]
result = reduce(lambda x, y: x + y**2, my_list, 0)

print(result)

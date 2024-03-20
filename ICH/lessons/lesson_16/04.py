# 4. Напишите программу, которая печатает ценник по параметрам:
# “The price of <product> is “X” Euro”. В строке <product> и <X> - параметры.
# Убедитесь, что цена выводится в Евро с центами
# (не более двух знаков после запятой).

product = input('Enter product name: ')
price = float(input('Enter product price: '))

print(f"The price of {product} is \"{price:.2f}\" Euro")

# Существует функция coffee(), которая варит кофе и если ее вызвать, то она
# печатает “кофе”. Декорировать эту функцию так, чтобы можно было варить кофе
# с сахаром, молоком или и тем и другим. Вызов декорируемой функции должен
# печатать, с чем кофе сварено. Сварить кофе с двойной порцией сахара и
# молока. Сварить двойной кофе.

def decorator(func):
    def wrapper(*args, **kwargs):
        if kwargs.get('double'):
            print('double', end=" ")

        func()

        with_milk = kwargs.get('milk')
        with_sugar = kwargs.get('sugar')
        milk_message = f'with {with_milk} portion of milk'
        sugar_message = f'with {with_sugar} portion of sugar'

        if with_milk and with_sugar:
            print(milk_message + sugar_message.replace("with", " and"), end=" ")
        else:
            if with_milk:
                print(milk_message, end=" ")
            if with_sugar:
                print(sugar_message, end=" ")
        print()

    return wrapper


@decorator
def coffee():
    print("coffee", end=" ")


coffee()
coffee(double=True)
coffee(milk=1)
coffee(milk=2)
coffee(shuger=2)
coffee(double=True, sugar=1)
coffee(double=True, milk=1, sugar=1)

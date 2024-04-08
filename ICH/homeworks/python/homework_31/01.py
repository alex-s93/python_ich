# 1. Напишите декоратор validate_args, который будет проверять типы аргументов функции и выводить сообщение об ошибке,
# если переданы аргументы неправильного типа. Декоратор должен принимать ожидаемые типы аргументов в качестве параметров
#
# Пример использования:
#
# @validate_args(int, str)
# def greet(age, name):
#     print(f"Привет, {name}! Тебе {age} лет.")
#
#
# greet(25, "Анна")  # Все аргументы имеют правильные типы
# greet("25", "Анна")  # Возникнет исключение TypeError
#
# Ожидаемый вывод:
#
# Привет, Анна! Тебе 25 лет.
# TypeError: Аргумент 25 имеет неправильный тип <class 'str'>. Ожидается <class 'int'>.

def validate_args(*types):
    def func_decorator(func):
        def wrapper(*values):
            if len(values) != len(types):
                raise ValueError(f"You have entered wrong number of arguments for validating. "
                                 f"Expected {len(values)}, got {len(types)}")

            for value, val_type in zip(values, types):
                if not isinstance(value, val_type):
                    raise TypeError(f'Argument {value} must be {val_type}. Got {type(value)} instead.')

            return func(*values)

        return wrapper

    return func_decorator


@validate_args(int, str)
def greet(age, name):
    print(f"Привет, {name}! Тебе {age} лет.")


greet(25, "Анна")
# greet("25", "Анна")


# Это пример валидатора с неправильным количеством типов для проверки. Будет следующее сообщение,
# если расскомментировать строку 57:
# ValueError: You have entered wrong number of arguments for validating. Expected 3, got 2
# @validate_args(str, float | int)
@validate_args(str, float | int, bool)
def bank_account(name, money_amount, married):
    print(f"Привет, {name}! У вас на счету {money_amount} денег. У вас есть супруг: {married}")


bank_account("Alex", 59, True)
# bank_account("Alex", 59.50, "yes")

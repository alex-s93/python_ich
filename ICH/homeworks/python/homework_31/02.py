# 2. Напишите декоратор log_args, который будет записывать аргументы и результаты вызовов функции в лог-файл.
# Каждый вызов функции должен быть записан на новой строке в формате "Аргументы: <аргументы>, Результат: <результат>".
# Используйте модуль logging для записи в лог-файл.
#
# Пример использования:
#
# @log_args
# def add(a, b):
#     return a + b
#
# add(2, 3)
# add(5, 7)
#
# Ожидаемый вывод в файле log.txt:
#
# Аргументы: 2, 3, Результат: 5
# Аргументы: 5, 7, Результат: 12
#
# Убедитесь, что перед запуском кода у вас создан файл log.txt в той же директории, где находится скрипт Python.

def check_log_file():
    file = None
    try:
        file = open("log.txt", "r")
    except FileNotFoundError:
        file = open("log.txt", "x")
    finally:
        file.close()


def write_log_file(value):
    with open("log.txt", "a") as file:
        file.write(value)


def log_args(func):
    def wrapper(*args, **kwargs):
        # NOTE: На самом деле - эта проверка не нужна. Функция open("log.txt", "a") создаст этот файл если его нету.
        # Но в условии задачи было дополнительно указано про проверку наличия файла.
        check_log_file()

        res = func(*args, **kwargs)

        write_log_file(f"Arguments: {str(args).replace('(', '').replace(')', '')}. Result: {res}.\n")

        return res

    return wrapper


@log_args
def add(a, b):
    return a + b


add(2, 3)
add(5, 7)

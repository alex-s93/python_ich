# У вас есть текстовый файл, где каждая строка - имя человека. Написать
# программу, которая выводит следующее приветствие:
# “Привет, <имя 1>, <имя 2>,... <имя n> и добро пожаловать!”. Программу
# реализовать с помощью генератора и суб-генератора, где суб-генератор
# возвращает имена из файла, а основной генератор в нужный момент считывает
# и возвращает значения из суб-генератора.
def names_gen(file):
    with open(file) as f:
        for line in f:
            yield line.strip()


def greeting_gen(file):
    names = []
    yield from (", ".join(names + [name]) + " и добро пожаловать!" for name in names_gen(file))
    # values = yield from names_gen()
    # yield f"Привет, {values} и добро пожаловать!"


for message in greeting_gen("names.txt"):
    print("Привет", message)

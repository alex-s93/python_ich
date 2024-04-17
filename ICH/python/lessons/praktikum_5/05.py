# Дан текстовый файл, где каждая строка описывает человека в формате:
# <Name>; <Age>
# Sergey;35
# Ivan;25
# Svetlana;20
# Maria;27
# Нужно написать программу, которая печатает имя самого старшего человека.
# Поменяйте программу так, чтобы она печатала список людей, чем возраст
# больше 25 лет.

def gen_oldest_man(file):
    people = None
    with open(file) as f:
        people = f.readlines()

    print(people)

    # return max([int(item.split(";")[1].strip()) for item in people])
    # return max(map(lambda x: x.split(";")[1].strip(), people))
    return list(filter(lambda x: int(x.split(";")[1].strip()) > 25, people))


print(gen_oldest_man("user_data.txt"))

#
# with open(FILENAME, "r") as file:
#     persons = {item[0]: item[1].strip() for item in map(lambda f: f.split(";"), file.readlines())}
#
# print(max(persons, key=lambda key: persons[key]))
# print(list(filter(lambda key: (int(persons[key]) > 25), persons)))

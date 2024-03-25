# 1. Напишите программу, которая подсчитывает количество вхождений каждого слова в тексте и выводит на экран наиболее
# часто встречающиеся слова. Для решения задачи используйте класс Counter из модуля collections.
# Создайте функцию count_words, которая принимает текст в качестве аргумента и возвращает словарь с количеством
# вхождений каждого слова. Выведите наиболее часто встречающиеся слова и их количество.
# Пример вывода:
#
# Введенный текст: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sed lacinia est.
# sed: 2
# Lorem: 1

from collections import Counter


def count_words(string):
    special_chars = "!@#$%^&*()[]{};:,./<>?\\|`~-=_+"
    without_special_chars = string.translate({ord(c): " " for c in special_chars})

    counter = Counter(without_special_chars.lower().split())
    return counter.most_common(2)


sentence = input("Enter a sentence: ")

print("The most repeated words are:")
for item in count_words(sentence):
    print(f"{item[0]}: {item[1]}")

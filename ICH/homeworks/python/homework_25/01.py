# 1. Напишите функцию find_longest_word, которая будет принимать список слов и возвращать самое длинное слово из списка.
# Аннотируйте типы аргументов и возвращаемого значения функции.
# Пример вызова функции и ожидаемого вывода:
#
# words = ["apple", "banana", "cherry", "dragonfruit"]
#
# result = find_longest_word(words)
#
# print(result)  # Ожидаемый вывод: "dragonfruit"

from typing import List
from collections import OrderedDict


def find_longest_word(word_list: List[str]) -> str:
    # NOTE: это рабочее классическое решение. Но решил попробовать другой подход.
    # longest_word = ""
    # for word in word_list:
    #     if len(word) > len(longest_word):
    #         longest_word = word
    # return longest_word

    sorted_dict = OrderedDict(sorted({len(word): word for word in word_list}.items()))

    return sorted_dict.popitem()[1]


words = ["apple", "banana", "cherry", "dragonfruit"]

result = find_longest_word(words)

print(result)

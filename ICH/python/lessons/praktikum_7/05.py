# Напишите программу, которая заменяет в тексте все слова, начинающиеся на
# ‘х’ или ‘f’ на звездочки. При чём количество звёздочек должно равняться
# количеству букв заменяемого слова
import re

string = """
X-Ray
Hello World! Forward to the main station. Would you like to install xenon on the car? Remove all papers from the xerox
"""


def my_func(match):
    return "*" * len(match.group(0))


new_string = re.sub(r'\b[xXfF][\w-]+\b', my_func, string)

print(new_string)

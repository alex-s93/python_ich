# 2. Напишите функцию highlight_keywords(text, keywords), которая выделяет все вхождения заданных ключевых слов в
# тексте, окружая их символами *. Функция должна быть регистронезависимой при поиске ключевых слов.
#
# Пример использования:
#
# text = "This is a sample text. We need to highlight Python and programming."
#
# keywords = ["python", "programming"]
#
# highlighted_text = highlight_keywords(text, keywords)
#
# print(highlighted_text)
# # Вывод: "This is a sample text. We need to highlight *Python* and *programming*."
import re


def highlight_keywords(sample_text, search_words):
    for keyword in search_words:
        pattern = re.compile(r'\b' + keyword, re.IGNORECASE)
        words = pattern.findall(sample_text)
        for word in set(words):
            sample_text = sample_text.replace(word, f'*{word}*')
    return sample_text


text = "This is a sample text. We need to highlight Python and programming. I like pYtHoN and ProGrammIng. Python"

keywords = ["python", "PROGRAMMING"]

highlighted_text = highlight_keywords(text, keywords)

print(highlighted_text)

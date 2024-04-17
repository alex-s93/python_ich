# Дана последовательность слов. Написать функцию, которая возвращает
# последовательность слов, в которой в словах длины 3 все буквы заглавные,
# а все слова начинающиеся на "q" или "f" исключены. Использовать цепочки.
# Пример: ["The", "quick", "brown", "fox"] -> ["THE", "quick"]
def custom_filter(collection):
    return list(map(lambda x: x.upper() if len(x) == 3 else x,
                    filter(lambda x: not x.lower().startswith(('q', 'f')), collection)))


strings = ["The", "quick", "brown", "fox"]
print(custom_filter(strings))

# Напишите программу, которая принимает список слов и возвращает список, содержащий только анаграммы.
# Анаграммы - это слова, составленные из одних и тех же букв, но в разном порядке.
# Создайте функцию anagrams, которая принимает список слов в качестве аргумента и возвращает список анаграмм.
# Используйте множества и сортировку букв в слове для проверки на анаграмму. Выведите результат на экран.
#
# Пример переданного списка слов:
# ['cat', 'dog', 'tac', 'god', 'act']
#
# Пример вывода:
# Анаграммы: ['dog', 'god'], ['cat', 'tac', 'act']

def get_anagrams(collection):
    anagrams = []
    for index, word in enumerate(collection):
        anagram = [word]

        for w in collection[index + 1::]:
            if set(word) == set(w):
                collection.remove(w)
                anagram.append(w)

        if len(anagram) > 1:
            anagrams.append(anagram)
    return anagrams


words = ['cat', 'dog', 'tac', 'god', 'act']

print("Anagrams: ", get_anagrams(words))

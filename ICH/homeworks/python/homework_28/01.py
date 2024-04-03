# Напишите программу, которая принимает список слов от пользователя и использует генераторное выражение (comprehension)
# для создания нового списка, содержащего только те слова, которые начинаются с гласной буквы. Затем программа должна
# использовать функцию map, чтобы преобразовать каждое слово в верхний регистр. В результате программа должна вывести
# новый список, содержащий только слова, начинающиеся с гласной буквы и записанные в верхнем регистре.

vowels = ('a', 'e', 'i', 'o', 'u')

# result = list(map(lambda word: word.strip().upper(), filter(lambda word: word.strip().lower().startswith(vowels),
#                                                             input("Enter some words, separated by comma: ").split(
#                                                                 ","))))

result = list(map(lambda word: word.strip().upper(),
                  [word for word in input("Enter some words, separated by comma: ").split(",") if
                   word.strip().lower().startswith(vowels)]))

print(result)

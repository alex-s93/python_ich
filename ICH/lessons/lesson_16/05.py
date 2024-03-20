# 5. Дана строка, состоящая из слов, разделенных пробелами. Определите,
# сколько в ней слов. Используйте для решения задачи метод count.

string = input("Enter some worlds separated by whitespace: ").strip()

words_amount = string.count(" ") + 1 if string else 0

print("Amount of words: ", words_amount)

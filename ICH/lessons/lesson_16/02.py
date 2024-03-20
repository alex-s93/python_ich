# 2. Написать программу, которая печатает True, если слова “cat” и “dog” встре-
# чаются в строке одинаковое количество раз (и напечатать false - если разное
# количество раз). 'catdog' → True, 'catcat' → False, '1cat1cadodog' → True

string = input("Enter a text: ")

cat_count = string.count("cat")
dog_count = string.count("dog")

print("The same count of dogs and cats: ", cat_count == dog_count)

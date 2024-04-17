# 1. Написать программу, которая выводит тег вокруг данного текста. Например,
# при вводе тега 'i' и строки 'Hello' получаем '<i>Hello</i>'

tag = input("Enter a tag: ")
string = input("Enter a string: ")

template = f"<{tag}>{string}<{tag}/>"

print(template)
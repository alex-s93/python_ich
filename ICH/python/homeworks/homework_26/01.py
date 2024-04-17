# 1. Напишите программу, которая принимает в качестве аргумента командной строки путь к файлу .py и запускает его.
# При запуске файла программа должна выводить сообщение "Файл <имя файла> успешно запущен". Если файл не существует или
# не может быть запущен, программа должна вывести соответствующее сообщение об ошибке.

from sys import argv

filepath = argv[1]

try:
    exec(open(filepath).read())
    print(f"File {filepath} was fired successfully")
except FileNotFoundError:
    # Try to open not-existing file e.g. test.txt
    print('File not found')
except UnicodeDecodeError:
    # Try to open the file img.png
    print('This file cannot be opened')

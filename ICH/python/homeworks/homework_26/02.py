# 2. Напишите программу, которая принимает в качестве аргумента командной строки путь к директории и выводит список всех
# файлов и поддиректорий внутри этой директории. Для этой задачи используйте модуль os и его функцию walk. Программа
# должна выводить полный путь к каждому файлу и директории.
from os import path, walk
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--dir-path", help="Path to directory")
args = parser.parse_args()

dir_path = args.dir_path

if path.exists(dir_path) and path.isdir(dir_path):
    for dirpath, dirnames, filenames in sorted(walk(dir_path)):
        if len(filenames) > 0:
            for filename in filenames:
                print(path.join(dirpath, filename))
        else:
            print(dirpath)
else:
    print("The entered path is not exist or is not a directory. Try again")

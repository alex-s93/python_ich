#!/bin/bash

# Скрипт для обработки лог-файлов:
# Разработайте скрипт, который анализирует лог-файлы сервера и извлекает информацию
# о возникших ошибках, записывая их в отдельный файл.

PATH_FROM="./log.log"
PATH_TO="./output.log"

if [ ! -f "$PATH_FROM" ]
then
  echo "$PATH_FROM file not found!"
  exit 1
fi

grep -i "error" "$PATH_FROM" >> "$PATH_TO"

echo "Done"

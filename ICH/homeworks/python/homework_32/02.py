# 2. Реализовать класс Email, представляющий электронное письмо. Класс должен поддерживать следующие операции:
#
# - Сравнение писем по дате (операторы <, >, <=, >=, ==, !=)
# - Преобразование письма в строку (метод __str__)
# - Получение длины текста письма (метод __len__)
# - Получение хеш-значения письма (метод __hash__)
# - Проверка наличия текста в письме (метод __bool__)
#
# Пример использования:
#
# email1 = Email("john@example.com", "jane@example.com", "Meeting", "Hi Jane, let's have a meeting tomorrow.", "2022-05-10")
# email2 = Email("jane@example.com", "john@example.com", "Re: Meeting", "Sure, let's meet at 2 PM.", "2022-05-10")
# email3 = Email("alice@example.com", "bob@example.com", "Hello", "Hi Bob, how are you?", "2022-05-09")
#
# print(email1)
# Вывод:
# """
# From: john@example.com
# To: jane@example.com
# Subject: Meeting
#
# Hi Jane, let's have a meeting tomorrow.
# """
#
# print(len(email2))  # Вывод: 24
# print(hash(email3))  # Вывод: -920444056
# print(bool(email1))  # Вывод: True
# print(email2 > email3)  # Вывод: True

from functools import total_ordering
from datetime import datetime


@total_ordering
class Email:
    date_format = "%Y-%m-%d"

    def __init__(self, sender, recipient, subject, body, date):
        self.__sender = sender
        self.__recipient = recipient
        self.__subject = subject
        self.__body = body
        self.__date = datetime.strptime(date, Email.date_format)

    def __hash__(self):
        return hash((self.__subject, self.__body))

    def __len__(self):
        return len(self.__body)

    def __bool__(self):
        return bool(self.__body)

    def __str__(self):
        return f"""
From: {self.__sender}
To: {self.__recipient}
Subject: {self.__subject}

{self.__body}"""

    def __eq__(self, other):
        return self.__date == other.__date

    def __lt__(self, other):
        return self.__date < other.__date


email1 = Email("john@example.com", "jane@example.com", "Meeting", "Hi Jane, let's have a meeting tomorrow.",
               "2022-05-10")
email2 = Email("jane@example.com", "john@example.com", "Re: Meeting", "Sure, let's meet at 2 PM.", "2022-05-10")
email3 = Email("alice@example.com", "bob@example.com", "Hello", "Hi Bob, how are you?", "2022-05-09")
email4 = Email("alice@example.com", "bob@example.com", "Hello", "Hi Bob, how are you?", "2022-05-09")
email5 = Email("alice@example.com", "bob@example.com", "Hello", "Hi Bob, how are you?", "2022-05-10")

print(len(email2))
print(hash(email3))
print(bool(email1))
print(email2 > email3)

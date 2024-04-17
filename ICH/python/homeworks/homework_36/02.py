# Напишите программу, которая запрашивает у пользователя URL-адрес веб-страницы и уровень заголовков, а затем использует
# библиотеку Beautiful Soup для парсинга HTML и извлекает заголовки нужного уровня (теги h1, h2, h3 и т.д.) с их текстом
import requests
from sys import exit
from bs4 import BeautifulSoup

if __name__ == "__main__":
    user_url = input("Enter a full url from which you wanna get the list of titles with specific level: ")
    title_level = input("Enter a title level (1-6): ")

    response = requests.get(user_url)

    if response.status_code != 200:
        print("The site is not reachable. Try again.")
        exit()

    soup = BeautifulSoup(response.text, "html.parser")

    elements = soup.find_all(f"h{title_level}")

    if len(elements) == 0:
        print(f"No titles with level {title_level}")
        exit()

    for element in elements:
        print(element.text.strip())

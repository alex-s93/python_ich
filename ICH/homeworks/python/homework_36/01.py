# Напишите программу, которая запрашивает у пользователя URL-адрес веб-страницы, использует библиотеку Beautiful Soup
# для парсинга HTML и выводит список всех ссылок на странице.

import requests
from sys import exit
from bs4 import BeautifulSoup

if __name__ == "__main__":
    user_url = input("Enter a full url from which you wanna get the list of links: ")

    response = requests.get(user_url)

    if response.status_code != 200:
        print("The site is not reachable. Try again.")
        exit()

    soup = BeautifulSoup(response.text, "html.parser")
    href_tags = soup.find_all(href=True)

    for element in href_tags:
        href = element['href']
        if href.startswith("http"):
            print(href)

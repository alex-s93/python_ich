# 2. Напишите функцию find_common_words(url_list), которая принимает список URL-адресов и возвращает список наиболее
# часто встречающихся слов на веб-страницах. Для каждого URL-адреса функция должна получить содержимое страницы с
# помощью запроса GET и использовать регулярные выражения для извлечения слов. Затем функция должна подсчитать
# количество вхождений каждого слова и вернуть наиболее часто встречающиеся слова в порядке убывания частоты.
import re
import requests
from collections import Counter


def find_common_words(url_list):
    pattern = re.compile(r'>([а-я\sёЁА-Яa-zA-ZöäüÖÄÜ!,.?-]+)</')

    common_words = Counter()
    for url in url_list:
        response = requests.get(url)
        if response.status_code == 200:
            text = " ".join(pattern.findall(response.text)).lower()
            array = re.sub(r"[$&+,:;=?@#|'<>.^*()%!-]", "", text).split()
            common_words += Counter(array)
        else:
            print(url, "-", response.status_code)

    return sorted(common_words.items(), key=lambda x: x[1], reverse=True)


if __name__ == '__main__':
    urls = ["https://itcareerhub.de", "https://itcareerhub.de/ru", "https://www.kaufland.de/"]
    result = find_common_words(urls)
    print("length of dictionary is:", len(result))
    for item, count in result:
        print(f"{item}: {count}")

# Написать на Python программу, которая узнает погоду в заданном городе.
# В интернете большое количество сервисов, которые “отдают” погоду через т.н.
# REST API. Работаем с сервисом Weather API. (Этот сервис бесплатный, но нужна
# регистрация и есть ограничение на количество запросов от одного пользователя
# в день). Скопируйте этот API Key и сохраните, он пригодится позже.
# интерактивный эксплорер: https://www.weatherapi.com/api-explorer.aspx
#
# Прежде, чем писать программу, нужно зарегистрироваться на сайте и найти в своем
# аккаунте свой API Key, который нужно отправлять с каждым запросом на сервер.
# API Key: 04430e1f9a4749bc9fd170739241304

import requests
import json

API_Key = '04430e1f9a4749bc9fd170739241304'
request_api = 'http://api.weatherapi.com/v1/current.json?key={}&q={}&aqi=no'


while True:
    city = input('Введите название города: ')
    response = requests.get(request_api.format(API_Key, city))

    if response.status_code == 200:
        data = json.loads(response.text)
        print('Город:', data['location']['name'])
        print('Страна:', data['location']['country'])
        print('Расположение:', data['location']['lat'], data['location']['lon'])
        print('Часовой пояс:', data['location']['tz_id'])
        print('Температура:', data['current']['temp_c'])
    else:
        print('Ошибка, статус отвута:', response.status_code)

    if input('Хотите выйти? (Y/Д): ').upper() in ('Y', 'Д'):
        break

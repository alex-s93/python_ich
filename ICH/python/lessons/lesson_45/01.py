import requests

response = requests.get("https://rozetka.com.ua/ua/test")
print(response.status_code)
print(response.text)
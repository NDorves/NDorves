# 1. Напишите программу, которая запрашивает у пользователя URL-адрес веб-страницы,
# использует библиотеку Beautiful Soup для парсинга HTML и выводит список всех ссылок на странице.
#
from bs4 import BeautifulSoup
import requests


def get_links_from_url(url):

        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            links = soup.find_all('a')
            for link in links:
                print(link.get('href'))

user_url = input("Введите URL-адрес: ")
get_links_from_url(user_url)

#
# # # 2. Напишите программу, которая запрашивает у пользователя URL-адрес веб-страницы и уровень заголовков,
# # # а затем использует библиотеку Beautiful Soup для парсинга HTML и извлекает заголовки нужного уровня
# # # (теги h1, h2, h3 и т.д.) с их текстом.
# #
# #
#
import requests
from bs4 import BeautifulSoup

url = input("Введите URL-адрес веб-страницы: ")
header_level = input("Введите уровень заголовков (например, h1, h2, h3 и т.д.): ")


def get_headers(url, header_level=None):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        headers = soup.find_all(header_level)
        for header in headers:
            print(f"{header.name}: {header.get_text()}")


get_headers(url, header_level)

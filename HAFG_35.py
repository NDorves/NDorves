# # 1. Напишите функцию get_response(url), которая отправляет GET-запрос по заданному URL-адресу
# # и возвращает объект ответа. Затем выведите следующую информацию об ответе:
# # - Код состояния (status code)
# # - Текст ответа (response text)
# # - Заголовки ответа (response headers)
# # Пример использования:
# # url = "https://api.example.com"
# # response = get_response(url)
# # print("Status Code:", response.status_code)
# # print("Response Text:", response.text)
# # print("Response Headers:", response.headers)

import requests
def get_response(url):
    response = requests.get(url)
    return response

# Пример использования:
url = "https://de.wikipedia.org/wiki/Simone_Biles"
response = get_response(url)
print("Status Code:", response.status_code)
print("Response Text:", response.text)
print("Response Headers:", response.headers)



#
# # 2. Напишите функцию find_common_words(url_list), которая принимает список URL-адресов и возвращает список
# # наиболее часто встречающихся слов на веб-страницах. Для каждого URL-адреса функция должна получить содержимое
# # страницы с помощью запроса GET и использовать регулярные выражения для извлечения слов.
# # Затем функция должна подсчитать количество вхождений каждого слова и вернуть наиболее часто встречающиеся слова
# # в порядке убывания частоты.
# #
# import requests
# import re
# from collections import Counter
#
# def find_common_words(url_list):
#     common_words = Counter()
#     for url in url_list:
#                 response = requests.get(url)
#                 words = re.findall(r'\b\w+\b', response.text.lower())
#                 common_words.update(words)
#
#     most_common = common_words.most_common()
#     return [word for word, count in most_common]
#
#
# url_list = ["https://de.wikipedia.org/wiki/Simone_Biles", "https://rapidapi.com/blog/movie-api/"]
# result = find_common_words(url_list)
# print("Наиболее распространенные слова:", result)

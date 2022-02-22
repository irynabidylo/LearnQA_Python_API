import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
number_of_responses = response.history
print(len(number_of_responses)) #3 количество редиректов
print(response.status_code) #итоговый ответ
print(response.url) #итоговый url


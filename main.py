import requests
from json.decoder import JSONDecodeError

#1
#parameters of the request:
#payload = {"name":"Ann"}

# response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
# print(response.text)

#2
#json отедельно не нужно импортировать, он входит в библиотеку requests
# response = requests.get("https://playground.learnqa.ru/api/hello", params={"name":"Anna"})
# parsed_response_text = response.json()
# print(parsed_response_text["answer"])

#3
# response = requests.get("https://playground.learnqa.ru/api/get_text")
# print(response.text)
# try:
#     parsed_answer = response.json()
#     print(parsed_answer)
# except JSONDecodeError:
#     print("Response is not in JSON format")

#4 параметры в URL передаются только в Get запросе после ? = example.com?param1=value1
#params used only for GET requests !!!
# response = requests.get("https://playground.learnqa.ru/api/check_type", params={"param1":"value1"})
# print(response.text)
# print(response.status_code)

#data is used for POST request, params don't work !!!
# response = requests.post("https://playground.learnqa.ru/api/check_type", data={"param1":"value1"})
# print(response.text)
# print(response.status_code)

#5
# response = requests.get("https://playground.learnqa.ru/api/get_500")
# print(response.status_code)
# print(response.text)

#6
#Редирект не идет и в ответе будут данные только первого запроса если allow_redirects=False
#а если True, то редирект идет и данные в переменной response будут только последнего ответа
# response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=False)
# print(response.status_code)

#чтобы узнать куда было перенаправлено используется функция history, она возвращет
#массив всех ответов, которые были получены до того как оказаться на итоговом URL

# response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
# first_response = response.history[0]
# second_response = response
# print(first_response)
# print(second_response)

#7
# headers = {"some_header":"123"}
# response = requests.get("https://playground.learnqa.ru/api/show_all_headers", headers=headers)
# print(response.text)
# print(response.headers)

# HEAD requests are done when you do not need the content of the file (body), but only the status_code or HTTP headers
# POST - It is often used when uploading a file or when submitting a completed web form.
# PUT method requests that the enclosed entity be stored under the supplied URI.
# If the URI refers to an already existing resource, it is modified and if the URI does not point
# to an existing resource, then the server can create the resource with that URI

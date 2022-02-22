import requests

#1 результат: выводится текст "Wrong method provided"
response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response.text)

#2 результат: выводится словарь:
#{'Date': 'Sun, 20 Feb 2022 19:59:13 GMT', 'Content-Type':
# 'text/html; charset=utf-8', 'Connection': 'keep-alive', 'Keep-Alive': 'timeout=10', 'Server': 'Apache'}
response = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response.headers)

#3 результат: выводится словарь: {"success":"!"}
response = requests.request("GET", "https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method":"GET"})
print(response.text)

#4
#два запроса на сервер, первый для GET с params, второй для всех остальных запросов с data
def request_to_server(method1, method2):
    if method1 == "GET":
        response = requests.request(method1, "https://playground.learnqa.ru/ajax/api/compare_query_type",
                                    params={"method":method2})
        return response.text
    else:
        response = requests.request(method1, "https://playground.learnqa.ru/ajax/api/compare_query_type",
                                    data={"method":method2})
        return response.text

#проверка всех возможных сочетаний реальных типов запроса и значений параметра method
def check_requests_and_methods():

    request_types = ["GET", "POST", "PUT", "DELETE"]
    index1 = 0

    while index1 < len(request_types):
        method1 = request_types[index1]
        index2 = 0
        while index2 <len(request_types):
            method2 = request_types[index2]
            response_text_from_server = request_to_server(method1, method2)

            if method1 == method2 and response_text_from_server == "Wrong method provided":
                print("Server says '\Wrong method provided'\ when %s = %s" %(method1, method2))

            elif method1 != method2 and response_text_from_server == '{"success":"!"}':
                print("Server says '\Success'\ when first method is %s and second method is %s" %(method1, method2))

            index2 += 1
        index1 += 1


check_requests_and_methods()

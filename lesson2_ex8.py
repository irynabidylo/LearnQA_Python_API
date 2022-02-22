import requests
import json
import time

#создавать задачу
response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
response_text = response.text
print(response_text)

#распарсить ответ для получения значения token
response_in_json_format = json.loads(response_text)
token_value = response_in_json_format["token"]
token = {"token":token_value}
print(token)

#2 один запрос с token ДО того, как задача готова
response2 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=token)
print(response2.text)

#убеждаемся в правильности поля status

assert response2.text == '{"status":"Job is NOT ready"}', "The job is not ready"

#ждем нужное количество секунд
seconds = response_in_json_format["seconds"]
time.sleep(seconds)

#4 делаем один запрос c token ПОСЛЕ того, как задача готова, убеждаемся в правильности поля status
# и наличии поля result
response3 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=token)
print(response3.text)

response3_in_json_format = json.loads(response3.text)
result = response3_in_json_format["result"]
status = response3_in_json_format["status"]

assert result == "42" and status =="Job is ready", "Job is not ready"
print("Job is ready. Result and status are correct")



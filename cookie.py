import requests

#1
payload = {"login":"secret_login", "password":"secret_pass"}
response = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)

print(response.text)
print(response.status_code)
#to get cookies
print(dict(response.cookies))
print(response.headers)

#2
payload = {"login":"secret_login", "password":"secret_pass"}
response1 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)

cookie_value = response1.cookies.get("auth_cookie")
print(cookie_value)

cookies = {}
#cookie_value will be None is login/password are wrong
if cookie_value is not None:
    cookies.update({"auth_cookie": cookie_value})
print(cookies)

response2 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies=cookies)
print(response2.text)


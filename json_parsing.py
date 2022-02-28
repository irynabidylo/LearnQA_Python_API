import json

string_json = '{"name": "Ann", "surname": "Brown", "age": 30}'
print(type(string_json)) #str
obj = json.loads(string_json)
print(type(obj)) #dict
print(obj) #dict
print(obj['name'])
print(obj['surname'])
print(obj['age'])

key = "age"

if key in obj:
    print(obj[key])
else:
    print(f"Key {key} is not in this JSON")

for key in obj:
    print(obj[key])

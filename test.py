#! /bin/python3
import requests
import json

res = requests.get('https://jsonplaceholder.typicode.com/todos/1')
print(res.status_code)
print(res.text)
jsonObj = json.loads(res.text)
print(jsonObj["title"])
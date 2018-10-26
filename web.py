import requests

par = {'key1': 'value1', 'key2': 'value2'}
url = 'http://www.example.com'
responce = requests.get(url)
print(responce.url)

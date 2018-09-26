import requests

url = 'http://www.google.com'
responce = requests.get(url)
print(responce.headers)

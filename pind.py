import requests
api = requests.get('http://api.open-notify.org/iss-now.json')
x = api.json()
print(x)

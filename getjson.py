import requests

headers = {
	'User-Agent' : 'Mozilla'
}

r = requests.get('https://www.ndtv.com', headers=headers)

returnedJson = r.json()

article = returnedJson['data']

for st in article:
	print(st['name'])

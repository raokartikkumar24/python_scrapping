import requests

headers = {
	'User-Agent' : 'Mozilla'
}

r = requests.get('https://www.ndtv.com', headers=headers)

returnedJson = r.json()

allStocks = returnedJson['data']

for st in allStocks:
	print(st['name'])

import requests

headers = {
	'User-Agent' : 'Mozilla'
}

r = requests.get('https://www.nse-india.com/api/equity-stockIndices?index=NIFTY%2050', headers=headers)

returnedJson = r.json()

allStocks = returnedJson['data']

for st in allStocks:
	print(st['symbol'], st['lastPrice'])
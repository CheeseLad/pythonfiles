'''imported required modules'''
import requests
import json


'''get current value of tesla and print to terminal'''
url = 'https://api.coinmarketcap.com/v1/ticker/tesla/'
response = requests.get(url)
data = response.json()
print (data[0]['price_usd'])
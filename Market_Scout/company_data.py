
import requests

fmp = "https://financialmodelingprep.com/api/v3/profile/IBM?apikey=vZjEVSQdbbyw7BmuAWHhrdgRIk1SiZHK"

response = requests.get(fmp)
data = response.json()

comp_data = data[0]

price = comp_data['price']
cName = comp_data['companyName']
sector = comp_data['sector']
ceo = comp_data['ceo']
country = comp_data['country']
img = comp_data['image']
exchange = comp_data['exchange']


#ALPHA VANTAGE
# SL28OI89P5479YAT

print(exchange)
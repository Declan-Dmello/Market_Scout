import requests

"""currency_data = requests.get("http://apilayer.net/api/live?access_key=c40203aea145c124a4edda196dcabcdd&currencies=EUR,GBP,INR,CNY,JPY,CHF,CAD,AUD,BRL,MXN,KRW,RUB,IDR,TRY,SAR,ZAR,PLN,THB,SEK,DKK,NOK&source=USD&format=1")

currency = currency_data.json()"""
top = ['USDEUR', 'USDGBP', 'USDINR', 'USDCNY', 'USDJPY', 'USDCHF', 'USDCAD', 'USDAUD', 'USDBRL', 'USDMXN']

top_curr1= ['EUR', 'GBP', 'INR', 'CNY', 'JPY','CHF', 'CAD', 'AUD', 'BRL', 'MXN']


flag1 = ['flags/Eu.jpeg','flags/UK.jpeg','flags/india.png','flags/china.png','flags/japan.png','flags/neutral.png','flags/canada.jpeg','flags/aus.jpeg','flags/brazil.png','flags/mexico.png']

#rates = currency['quotes']

#API key Financial modelling
#vZjEVSQdbbyw7BmuAWHhrdgRIk1SiZHK

#dic_rates = dict(rates)
#curr_list = list(dic_rates.keys())
#currval_list =list(dic_rates.values())[:10]
currval_list= [0.93, 0.79,83.04, 7.20,149.26, 0.87,  1.35,  1.54, 4.95, 17.09]






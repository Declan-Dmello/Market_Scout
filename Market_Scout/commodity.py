import humanize
from PyQt6.QtGui import QPixmap

"""
import requests

crypto = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=Bitcoin%2CEthereum%2CTether%2"
                      "CBinancecoin%2CCardano%2CSolana%2CDogecoin%2CMatic%2CRipple&vs_curre"
                      "ncies=USD&include_market_cap=true&include_24hr_change=true&include_last_updated_at=true&precision=2")

# put images , download them and put (tell someone in the team to do)
crypto_data = crypto.json()
print(crypto_data)"""
coins = []
coins_price = [325.42,47632.73,0.55,0.08,2518.14,0.52,106.29,1.0]
coins_mcap_0 =[50051617636.149315,934348461753.1996,19192791674.225517,11750680868.261173,302197613494.65326,28522697577.598335,46238874097.20198,96201453651.66331]
coin_change = [1.8748152932349,  4.941004162252546, 2.0648005796184803,1.253337836692083,3.046860983185483,0.9634202282307446,1.2786740921649573,0.12043582340078025]
coins_mcap = []

for i in coins_mcap_0:
    coins_mcap.append(humanize.intword(i) + " $")
"""
for i in crypto_data:
    j = i.capitalize()
    coins.append(j)
"""

coins = ['Binancecoin', 'Bitcoin', 'Cardano', 'Dogecoin', 'Ethereum', 'Ripple', 'Solana', 'Tether']

coins_logo =  ["images/crypto/binancecoin (1).png","images/crypto/bitcoin (1).png","images/crypto/cardano (1).png","images/crypto/dogecoin (1).png","images/crypto/etherum (1).png","images/crypto/ripple (1).png","images/crypto/solana (1).png","images/crypto/tether (1).png"]


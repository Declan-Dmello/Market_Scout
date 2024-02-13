"""import yfinance as yf


index_codes = [
    "^GSPC",  # S&P 500
    "^IXIC",  # Nasdaq Composite
    "^GDAXI",  # DAX
    "^FCHI",  # CAC 40
    "^FTSE",  # FTSE 100
    "^HSI",   # Hang Seng Index
    "^BSESN",
    "S68.SI",
    "^NSEI",
    "^N225"

]

data = []

for i in index_codes:
    data.append(yf.Ticker(i))
print(data)


a =[]
b = 0
for i in data:
    a.append(i.info)
    print(i.info)


name = []
for i in a:
    print(i)
    name.append(i['open'])
    print("done")

print(name)
"Timezone - previous close - long name - symbol- exchange - currency"""

st_long_name = ['S&P 500', 'NASDAQ Composite', 'DAX PERFORMANCE-INDEX', 'CAC 40', 'FTSE 100', 'HANG SENG INDEX', 'S&P BSE SENSEX', 'Singapore Exchange Limited', 'NIFTY 50', 'Nikkei 225']
st_points = [5004.17, 15842.379, 16973.58, 7652.45, 7595.48, 15709.3, 71410.29, 9.19, 21727.0, 36915.44]
st_curr = ['USD', 'USD', 'EUR', 'EUR', 'GBP', 'HKD', 'USD', 'SGD', 'INR', 'JPY']
st_symbol=['^GSPC', '^IXIC', '^GDAXI', '^FCHI', '^FTSE', '^HSI', '^SSE', 'S68.SI', '^NSEI', '^N225']
st_exchange = ['SNP', 'NIM', 'GER', 'PAR', 'FGI', 'HKG', 'WCB', 'SES', 'NSI', 'OSA']
st_timezone = ['America/New_York', 'America/New_York', 'Europe/Berlin', 'Europe/Paris', 'Europe/London', 'Asia/Hong_Kong', 'America/New_York', 'Asia/Singapore', 'Asia/Kolkata', 'Asia/Tokyo']
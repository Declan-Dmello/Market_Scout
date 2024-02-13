"""import requests
from bs4 import BeautifulSoup

url = "https://www.nseindia.com/market-data/top-gainers-losers"

resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')

tables = soup.find_all('table')[1:3]

for table in tables:
    # parse table rows
    print(table.text)

"""

g_symbol        = ["GRASIM", "SBIN", "APOLLOHOSP", "SUNPHARMA", "ICICIBANK", "ADANIPORTS", "HEROMOTOCO", "BRITANNIA", "AXISBANK", "CIPLA"]
g_open          =[2057.25, 703.65, 6269.40, 1500.90, 988.85, 1252.60, 4840.00, 4875.55, 1039.95, 1428.10]
g_high         = [2182.00, 728.35, 6473.95, 1539.00, 1013.75, 1275.50, 4924.00, 4978.05, 1054.90, 1447.55]
g_low          = [2046.90, 694.20, 6213.60, 1492.25, 985.50, 1232.10, 4792.10, 4860.05, 1034.55, 1417.05]
g_prev_close   =  [2057.30, 699.55, 6231.00, 1499.60, 989.30, 1245.20, 4807.90, 4875.55, 1035.90, 1420.20]
g_chg           = [5.92, 3.70, 3.25, 2.80, 2.19, 2.18, 2.02, 1.88, 1.61, 1.53]


l_symbol =  [ "M&M",  "BHARTIARTL", "NTPC", "ONGC"," TATASTEEL", "HINDALCO", "INFY", "JSWSTEEL", "SBILIFE", "POWERGRID"]

l_open =   [1686.00, 1145.95, 332.95, 275.00, 144.20, 601.00, 1684.70, 824.90, 1468.00, 278.60]
l_high =  [1689.75, 145.95, 335.00, 275.65, 144.45, 602.00, 1692.90, 825.00, 1468.00, 279.45]
l_low =   [1628.00, 1116.25, 319.60, 259.15, 139.15, 576.30, 1659.80, 800.45, 1436.50, 269.10]
l_prev_close =  [1685.90, 1142.15, 330.90, 273.15, 143.65, 601.30, 1692.10, 822.10, 1459.05, 276.20]
l_chg = [-2.46, -1.94, -1.87, -1.85, -1.64, -1.48, -1.31, -1.25, -1.17, -1.16]
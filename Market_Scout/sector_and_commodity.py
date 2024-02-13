"""import requests
from bs4 import BeautifulSoup
import pandas as pd
r = requests.get("https://api.scrapingdog.com/scrape?api_key=65a17ccdad957e17f0697f8b&url=https://finance.yahoo.com/sectors").text
soup = BeautifulSoup(r, 'html.parser')
alldata = soup.find_all("tbody")

table1 = alldata[0].find_all("tr")

l1 ={}
l2 ={}
u1 = []
u2 = []

for i in range(0,len(table1)):
    table_td= table1[i].find_all("td")
    l1[table_td[0].text] = table_td[1].text
    l2[table_td[2].text] = table_td[3].text

u1.append(l1)
u2.append(l2)

a = u1[0]
b = u2[0]
print(a)
print(b)

print("---------------")
#----------------------------------------------------------------------------------------------


r1 = requests.get("https://api.scrapingdog.com/scrape?api_key=5ea541dcacf6581b0b4b4042&url=https://tradingeconomics.com/").text
soup1 = BeautifulSoup(r1, 'html.parser')

table = soup1.find("table", class_="table table-condensed")
#print(table)



data = []
for row in table.find_all("tr"):
    row_data = []
    for cell in row.find_all(["td", "th"]):
        row_data.append(cell.text.strip())
    data.append(row_data)

print(data)
df = pd.DataFrame(data)
print(df)
"""


commodity =  ['Crude Oil', 'Brent', 'Natural gas', 'Gasoline', 'Heating Oil', 'Gold', 'Silver', 'Copper', 'Soybeans', 'Wheat', 'Coal', 'Steel', 'Iron Ore', 'TTF Gas', 'Lumber']
commo_price  = [76.624, 81.981, 1.8359, 2.3416, 2.9676, 2022.58, 22.475, 3.6878, 1186.00, 598.16, 120.00, 3901.00, 128.00, 26.80, 552.96]
commo_change =  [0.40, 0.35, 0.08, 0.00, 0.08, 10.60, 0.10, 0.02, 7.50, 9.66, 0.50, 17.00, 0.00, 1.02, 2.46]
commo_change_percent = ['0.53%', '0.43%', '-4.23%', '-0.02%', '2.66%', '-0.52%', '-0.45%', '-0.48%', '-0.63%', '1.64%', '-0.41%', '0.44%', '0.00%', '-3.66%', '0.45%']



sector = ['All Sectors','Technology','Financial Services','Healthcare','Consumer Cyclical','Industrials','Communication Services','Consumer Defensive','Energy','Basic Materials', 'Real Estate','Utilities']
sector_p = ['100%','27.84%', '14.33%','11.60%','11.06%','9.00%', '8.68%','5.53%', '4.78%','2.65%','2.58%',  '1.96%']
sector_change1d = ['0.60%' , '1.58%', '0.47%', '0.01%', '1.03%', '0.34%', '0.59%', '-0.90%', '-1.08%', '-0.15%', '0.39%']
sector_change1y = [ '4.10%', '9.40%',  '2.05%', '-4.58%',  '2.16%',  '1.99%',  '9.33%',  '1.50%', '-2.22%',  '-4.33%','-5.29%']


#CG-buTw1yZuUueKAjHCQJJEgtDh
#crypto api key (Gecko)



"""
gmail_user = 'marketscout2@gmail.com'
gmail_password = 'mavv okip gbnj myjb '
"""
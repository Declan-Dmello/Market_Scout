import datetime
import nltk
import yfinance as yf
#from transformers import pipeline

#summarizer = pipeline("summarization", model="Falconsai/text_summarization")

import pytz

data = yf.Ticker('HDFCBANK.NS').info
print(data)
comp_name = data['shortName']
comp_data_main = []
for key in ['firstTradeDateEpochUtc', 'currency', 'currentPrice', 'previousClose',
            'timeZoneFullName', 'fullTimeEmployees', 'companyOfficers', 'open']:
    try:
        if key == 'companyOfficers':
            comp_data_main.append(data[key][0]['title'])
            comp_data_main.append(data[key][0]['name'])
        else:
            comp_data_main.append(data[key])
    except KeyError:
        comp_data_main.append("NA")


comp_data_1 = []
for key in ['city', 'industry', 'marketCap', 'country', 'sector', 'exchange']:
    try:
        comp_data_1.append(data[key])
    except KeyError:
        comp_data_1.append("NA")

comp_risk_factor = []
for key in ['auditRisk','boardRisk','compensationRisk','shareHolderRightsRisk']:
    try:
        comp_risk_factor.append(data[key])
    except KeyError:
        comp_risk_factor.append("NA")

comp_stock_prices_data = []
for key in ['previousClose', 'open', 'dayLow', 'dayHigh', 'bid', 'ask', 'askSize', 'bidSize', 'fiftyTwoWeekLow', 'fiftyTwoWeekHigh']:
    try:
        comp_stock_prices_data.append(data[key])
    except KeyError:
        comp_stock_prices_data.append("NA")

comp_financial_data = []
for key in ['pegRatio', 'beta', 'trailingPE', 'forwardPE', 'debtToEquity', 'returnOnEquity',
            'earningsGrowth', 'revenueGrowth', 'profitMargins', 'grossProfits']:
    try:
        comp_financial_data.append(data[key])
    except KeyError:
        comp_financial_data.append("NA")

comp_analyst_data = []
for key in ['targetHighPrice', 'targetLowPrice', 'recommendationKey']:
    try:
        comp_analyst_data.append(data[key])
    except KeyError:
        comp_analyst_data.append("NA")

comp_market_data = []
for key in ['volume', 'bookValue', 'mostRecentQuarter', 'earningsQuarterlyGrowth',
            'totalCash', 'totalDebt']:
    try:
        comp_market_data.append(data[key])
    except KeyError:
        comp_market_data.append("NA")
business_summary = data['longBusinessSummary']

#bs = "Tesla, Inc. designs, develops, manufactures, leases, and sells electric vehicles, and energy generation and storage systems in the United States, China, and internationally. It operates in two segments, Automotive, and Energy Generation and Storage. The Automotive segment offers electric vehicles, as well as sells automotive regulatory credits; and non-warranty after-sales vehicle, used vehicles, retail merchandise, and vehicle insurance services. This segment also provides sedans and sport utility vehicles through direct and used vehicle sales, a network of Tesla Superchargers, and in-app upgrades; purchase financing and leasing services; services for electric vehicles through its company-owned service locations and Tesla mobile service technicians; and vehicle limited warranties and extended service plans. The Energy Generation and Storage segment engages in the design, manufacture, installation, sale, and leasing of solar energy generation and energy storage products, and related services to residential, commercial, and industrial customers and utilities through its website, stores, and galleries, as well as through a network of channel partners; and provision of service and repairs to its energy product customers, including under warranty, as well as various financing options to its solar customers. The company was formerly known as Tesla Motors, Inc. and changed its name to Tesla, Inc. in February 2017. Tesla, Inc. was incorporated in 2003 and is headquartered in Austin, Texas."
"""
print(summarizer(business_summary, max_length=230, min_length=80, do_sample=False))
"""

#nltk.download("punkt")  # Download the sentence tokenizer
sentences = nltk.sent_tokenize(business_summary)

#summary  = sentences
#summary  = summarizer(business_summary, max_length=300, min_length=250, do_sample=False)[0]['summary_text']

index_sent = [0,1,2,3,4]
summary = ""
for i in sentences:
    if sentences.index(i) in index_sent:
        summary += " " + i







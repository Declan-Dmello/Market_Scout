import yfinance as yf
import tal
import pandas as pd
import numpy as np

# Download data
data = yf.download('GOOG', period='5y')

# Calculate metrics
data['Return'] = data['Adj Close'].pct_change()
data['Lag_Return'] = data['Return'].shift(1)
data['Lag_Volume'] = data['Volume'].shift(1)
data['Vol_SMA10'] = talib.SMA(data['Volume'], 10)
data['Daily_Change'] = (data['Close'] - data['Open']) / data['Open'] * 100

# Categorize weekdays
data['Weekday'] = pd.to_datetime(data.index).dayofweek
data['Weekday'] = data['Weekday'].apply(lambda x: 1 if x<5 else 0)

# Generate directional targets
data['Direction'] = np.where(data['Return'].shift(-1) > 0,  1, 0)

# Final feature columns
features = ['Return', 'Lag_Return', 'Daily_Change', 'Weekday',
            'Volume', 'Vol_SMA10', 'Lag_Volume']

# Target variable
target = data['Direction']
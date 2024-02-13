import yfinance as yf
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,Normalizer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier,ExtraTreesClassifier,AdaBoostClassifier
from sklearn import metrics
from sklearn.svm import SVC
import time
from xgboost import XGBClassifier


graph_data = yf.Ticker('GOOG')
df = pd.DataFrame(graph_data.history(period="max", interval="1d"))
df.drop(columns=[ 'Dividends', 'Stock Splits'], inplace=True)

st = time.time()

df['open-close'] = df['Open'] - df['Close']
df['low-high'] = df['Low'] - df['High']

df['target'] = np.where(df['Volume'].shift(-1) < df['Volume'], 1, 0)

print(df)

features = df[['open-close', 'low-high']]
target = df['target']
print(features)


scaler = StandardScaler()
features = scaler.fit_transform(features)

print(features)

X_train, X_valid, Y_train, Y_valid = train_test_split(
	features, target, test_size=0.1, random_state=2022)#2022
print(X_train.shape, X_valid.shape)

"""
models = [RandomForestClassifier(),ExtraTreesClassifier(),XGBClassifier(),SVC(probability=True),LogisticRegression()]
for i in models:
	i.fit(X_train, Y_train)
	print(str(i))
	print('Training Accuracy : ', metrics.roc_auc_score(
		Y_train, i.predict_proba(X_train)[:, 1]))
	print('Validation Accuracy : ', metrics.roc_auc_score(
		Y_valid, i.predict_proba(X_valid)[:, 1]))
"""
en = time.time()
print(en-st)

modell = AdaBoostClassifier()
modell.fit(X_train,Y_train)
y_pred = modell.predict(X_valid)
print(y_pred)

data11 = graph_data.info
a = data11['dayHigh'] - data11['dayLow']
b = data11['previousClose'] - data11['open']
c = {"a":a,
	 "b":b}

dataset1 = pd.DataFrame(c,index=[0])
#dataset = scaler.fit_transform(dataset1)
print(dataset1)
#fea = dataset1['a','b']
#fea =  scaler.tr
#features1 = arr[['open-close', 'low-high']]
#print(features1)
print("Prediction!")
m_ouput = modell.predict(dataset1)
m_ouput1 = modell.predict_proba(dataset1)
print(m_ouput)
print(m_ouput1)

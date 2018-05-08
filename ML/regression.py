import pandas as pd
import quandl, math
import numpy as np
from sklearn import preprocessing, svm, model_selection
from sklearn.linear_model import LinearRegression

# df = data frames

df = quandl.get("WIKI/GOOGL", authtoken="TyEbxAPfys-6d4nniV66")


df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]

df['HL_PCT'] = ((df['Adj. High'] - df['Adj. High']) / df['Adj. Close']) * 100.00

df['PCT_change'] = ((df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open']) * 100.00

df = df[['Adj. Close','HL_PCT','PCT_change', 'Adj. Volume']] # features

forecast_col = 'Adj. Close'
df.fillna(-99999, inplace=True)

forecast_out = int(math.ceil(0.01*len(df)))

df['label'] = df[forecast_col].shift(-forecast_out) # labels
df.dropna(inplace=True)

print df.tail()

# print df.head()

# Features = X , label = y

X = np.array(df.drop(['label'], 1))
y = np.array(df['label'])

X = preprocessing.scale(X)
y = np.array(df['label'])

X_sample, X_test, y_sample, y_test = model_selection.train_test_split(X, y, test_size=0.2)

# Classifies
clf = LinearRegression()
clf.fit(X_sample, y_sample)

# accuracy
acc = clf.score(X_test, y_test)
print acc

#
import pandas as pd
import quandl, math, datetime
import numpy as np
from sklearn import preprocessing, svm, model_selection
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot, style

style.use('ggplot')

# df = data frames

df = quandl.get("WIKI/GOOGL", authtoken="TyEbxAPfys-6d4nniV66")


df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]

df['HL_PCT'] = ((df['Adj. High'] - df['Adj. High']) / df['Adj. Close']) * 100.00

df['PCT_change'] = ((df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open']) * 100.00

df = df[['Adj. Close','HL_PCT','PCT_change', 'Adj. Volume']] # features

forecast_col = 'Adj. Close'
df.fillna(-99999, inplace=True) # handling NANs

forecast_out = int(math.ceil(0.01*len(df)))

print "Forecast for ", forecast_out, "days"

df['label'] = df[forecast_col].shift(-forecast_out) # labels


print df.tail()

# print df.head()

# Features = X , label = y

X = np.array(df.drop(['label'], 1))
X = preprocessing.scale(X)
X = X[:-forecast_out]
X_lately = X[-forecast_out:]

df.dropna(inplace=True)
y = np.array(df['label'])
y = np.array(df['label'])

X_sample, X_test, y_sample, y_test = model_selection.train_test_split(X, y, test_size=0.2)

# Classifies
clf = LinearRegression(n_jobs=2) # Regression | n_jobs default is 1 and -1 is for the end
# clf = svm.SVR() # SVM
clf.fit(X_sample, y_sample)

# accuracy
acc = clf.score(X_test, y_test) # test

forecast_set = clf.predict(X_lately)

print "Accuracy is ", acc

print forecast_set, acc, forecast_out

df['Forecast'] = np.nan

last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
single_day = 86400
next_unix = last_unix + single_day

for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += single_day
    df.loc[next_date] = [np.nan for _ in xrange(len(df.columns)-1)] + [i]

# print df.head()
# print df.tail()

df['Adj. Close'].plot()
df['Forecast'].plot()
pyplot.legend(loc = 4)
pyplot.title('Stock Market Price Prediction')
pyplot.xlabel('Date')
pyplot.ylabel('Price')
''' pyplot.savefig('ML/Plots/plot.png')
pyplot.show()
 '''
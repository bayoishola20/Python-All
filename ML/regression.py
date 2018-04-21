import pandas as pd
import quandl
import math

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

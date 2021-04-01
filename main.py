import datetime as dt
#from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.sectorperformance import SectorPerformances
from alpha_vantage.cryptocurrencies import CryptoCurrencies
from alpha_vantage.foreignexchange import ForeignExchange
import os
from dotenv import load_dotenv, find_dotenv
from pprint import pprint
import urllib.request, json
import numpy as np
#import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler

load_dotenv(find_dotenv())

ts = TimeSeries(key = os.environ.get('ALPHA_VANTAGE_API_KEY'), output_format='pandas')
sp = SectorPerformances(key = os.environ.get('ALPHA_VANTAGE_API_KEY'), output_format='pandas')
cc = CryptoCurrencies(key=os.environ.get('ALPHA_VANTAGE_API_KEY'), output_format='pandas')
fx = ForeignExchange(key=os.environ.get('ALPHA_VANTAGE_API_KEY'))

#Stocks
#data, meta_data = ts.get_intraday(symbol='TSLA', interval='1min', outputsize='full')
#pprint (data.head(10))
#data['4. close'].plot()
#plt.title('aaa')
#plt.tight_layout()
#plt.grid()
#plt.show()

#Sector
#data, meta_data = sp.get_sector()
#data['Rank A: Real-Time Performance'].plot(kind='bar')
#plt.title('Real Time Performance (%) per Sector')
#plt.tight_layout()
#plt.grid()
#plt.show()

#Crypto
#data, meta_data = cc.get_digital_currency_daily(symbol='BTC', market='CNY')
#data['4b. close (USD)'].plot()
#plt.tight_layout()
#plt.title('Daily close value for bitcoin (BTC)')
#plt.grid()
#plt.show()

#Forex
#data, _ = fx.get_currency_exchange_rate(from_currency='BTC',to_currency='USD')
#pprint(data)

#storing data in a file
ticker = "AAL"
file_to_save = 'stock_market_data-%s.csv'%ticker

if not os.path.exists(file_to_save):
    data, meta_data = ts.get_daily(symbol=ticker, outputsize='full')
    data.to_csv(file_to_save)
    print('Data saved to: %s' %file_to_save)
else:
    print('Loading data from: ' + file_to_save)
    df = pd.read_csv(file_to_save)

#sorting by date
df = df.sort_values('date')
#print (df.head())

#plt.figure(figsize = (19,9))
#plt.plot(range(df.shape[0]),(df['3. low']+df['2. high'])/2.0)
#plt.xticks(range(0,df.shape[0],500),df['date'].loc[::500],rotation=45)
#plt.xlabel('date',fontsize=18)
#plt.ylabel('Mid Price',fontsize=18)
#plt.show()

#Data sets
high = df.loc[:,'2. high'].to_numpy()
low= df.loc[:,'3. low'].to_numpy()
mid = (high+low)/2.0
#print (mid)
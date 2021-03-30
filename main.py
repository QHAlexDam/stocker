import datetime as dt
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

load_dotenv(find_dotenv())

ts = TimeSeries(key = os.environ.get('ALPHA_VANTAGE_API_KEY'), output_format='pandas', indexing_type='date')
sp = SectorPerformances(key = os.environ.get('ALPHA_VANTAGE_API_KEY'), output_format='pandas')
cc = CryptoCurrencies(key=os.environ.get('ALPHA_VANTAGE_API_KEY'), output_format='pandas')
fx = ForeignExchange(key=os.environ.get('ALPHA_VANTAGE_API_KEY'))

#Stocks
data, meta_data = ts.get_intraday(symbol='TSLA', interval='1min', outputsize='full')
pprint (data.head(10))
data['4. close'].plot()
plt.title('aaa')
plt.tight_layout()
plt.grid()
plt.show()

#Sector
data, meta_data = sp.get_sector()
data['Rank A: Real-Time Performance'].plot(kind='bar')
plt.title('Real Time Performance (%) per Sector')
plt.tight_layout()
plt.grid()
plt.show()

#Crypto
data, meta_data = cc.get_digital_currency_daily(symbol='BTC', market='CNY')
data['4b. close (USD)'].plot()
plt.tight_layout()
plt.title('Daily close value for bitcoin (BTC)')
plt.grid()
plt.show()

#Forex
data, _ = fx.get_currency_exchange_rate(from_currency='BTC',to_currency='USD')
pprint(data)

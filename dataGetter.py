from imports import *

#ticker:string ex 'TSLA'
#timeInterval:string ex '1min'
def getStockIntraday(stockTicker, timeInterval):
    ts = TimeSeries(key = os.environ.get('ALPHA_VANTAGE_API_KEY'), output_format='pandas')
    data, meta_data = ts.get_intraday(symbol=stockTicker, interval=timeInterval, outputsize='full')
    #pprint (data.head(10))
    #data['4. close'].plot()
    #plt.title('aaa')
    #plt.tight_layout()
    #plt.grid()
    #plt.show()
    return(data, meta_data)

def getStockDaily(stockTicker):
    ts = TimeSeries(key = os.environ.get('ALPHA_VANTAGE_API_KEY'), output_format='pandas')
    data, meta_data = ts.get_daily(symbol=stockTicker, outputsize='full')
    return(data, meta_data)

def getSectorData():
    sp = SectorPerformances(key = os.environ.get('ALPHA_VANTAGE_API_KEY'), output_format='pandas')
    data, meta_data = sp.get_sector()
    #data['Rank A: Real-Time Performance'].plot(kind='bar')
    #plt.title('Real Time Performance (%) per Sector')
    #plt.tight_layout()
    #plt.grid()
    #plt.show()
    return(data, meta_data)     

#ticker:string ex 'BTC'
#timeInterval:string ex 'CNY'
def getCryptoData(ticker, marketName):
    cc = CryptoCurrencies(key=os.environ.get('ALPHA_VANTAGE_API_KEY'), output_format='pandas')
    data, meta_data = cc.get_digital_currency_daily(symbol=ticker, market=marketName)
    #data['4b. close (USD)'].plot()
    #plt.tight_layout()
    #plt.title('Daily close value for bitcoin (BTC)')
    #plt.grid()
    #plt.show()
    return(data, meta_data)

#ex. from 'BTV' to 'USD'
def getForexData(fromCurr, toCurr):
    fx = ForeignExchange(key=os.environ.get('ALPHA_VANTAGE_API_KEY'))
    data, _ = fx.get_currency_exchange_rate(from_currency=fromCurr,to_currency=toCurr)
    return(data)


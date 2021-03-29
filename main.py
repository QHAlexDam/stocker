import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
from alpha_vantage.timeseries import TimeSeries
API = 'YA4TQBJDMX3RG00Q'

style.use('ggplot')

#start = dt.datetime(2021, 1, 1)
#end = dt.datetime.now()

#df = web.DataReader("GME", 'AlphaVantage', start, end)

ts = TimeSeries(key=API)
# Get json object with the intraday data and another with  the call's metadata
data, meta_data = ts.get_intraday('GME')

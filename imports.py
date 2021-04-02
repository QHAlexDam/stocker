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
import math
#import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler\

from standardAverage import *
from dataGetter import *
from dataExport import *
from dataSets import *
from exponentialMovingAvg import *
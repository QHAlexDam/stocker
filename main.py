from imports import *
load_dotenv(find_dotenv())

#INPUT DATA
STOCK_TICKER = "TSLA"
FILE_NAME = 'stock_market_data-%s.csv'%STOCK_TICKER
#values depend on sample size
WINDOW_SIZE = 300  # we want 4 windows within a data set (2 data sets, each representing half of the total data pool)
RANGE_INIT = 0
RANGE_END = 1200 # 4* window size

#Getting and storing data in a cvs file
df = stockToCSV(FILE_NAME, STOCK_TICKER)

#creating data sets
scaler, trainingData, testingData, all_mid_data  = createDataSets(df, WINDOW_SIZE, RANGE_INIT, RANGE_END)

#standard average
windowSize = math.floor(WINDOW_SIZE/25)
std_avg_prediction(df, trainingData, all_mid_data, windowSize)

#exponential moving average
exp_mov_avg_prediction(df, trainingData, all_mid_data)

#model
LSTM(trainingData, 5, 5)

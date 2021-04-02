from imports import *
load_dotenv(find_dotenv())

#INPUT DATA
STOCK_TICKER = "TSLA"
FILE_NAME = 'stock_market_data-%s.csv'%STOCK_TICKER
#values depend on sample size
WINDOW_SIZE = 300 
RANGE_INIT = 0
RANGE_END = 1200

#Getting and storing data in a cvs file
df = stockToCSV(FILE_NAME, STOCK_TICKER)

#creating data sets
scaler, trainingData, testingData, all_mid_data  = createDataSets(df, WINDOW_SIZE, RANGE_INIT, RANGE_END)

#standard average
std_avg_prediction(df, trainingData, all_mid_data)


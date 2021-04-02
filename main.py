from imports import *
load_dotenv(find_dotenv())

#Getting and storing data in a cvs file
ticker = "AAL"
file_to_save = 'stock_market_data-%s.csv'%ticker
df = stockToCSV(file_to_save, ticker)

#Graphing data
#plt.figure(figsize = (19,9))
#plt.plot(range(df.shape[0]),(df['3. low']+df['2. high'])/2.0)
#plt.xticks(range(0,df.shape[0],500),df['date'].loc[::500],rotation=45)
#plt.xlabel('date',fontsize=18)
#plt.ylabel('Mid Price',fontsize=18)
#plt.show()

winSize = 400
rangei=0
rangef=1600

scaler = createDataSets(df, winSize, rangei, rangef)[0]
trainingData = createDataSets(df, winSize, rangei, rangef)[1]
testingData = createDataSets(df, winSize, rangei, rangef)[2]
all_mid_data = createDataSets(df, winSize, rangei, rangef)[3]


#standard average
std_avg_prediction(df, trainingData, all_mid_data)


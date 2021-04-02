from imports import *
load_dotenv(find_dotenv())

#Getting and storing data in a cvs file
ticker = "AAL"
#url_string = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=%s&outputsize=full&apikey=%s"%(ticker,os.environ.get('ALPHA_VANTAGE_API_KEY'))
file_to_save = 'stock_market_data-%s.csv'%ticker
if not os.path.exists(file_to_save):
    data = getStockDaily('AAL')[0]
    data.to_csv(file_to_save)
    print('Data saved to: %s' %file_to_save)
    df = pd.read_csv(file_to_save)
    df = df.sort_values('date')
else:
    print('Loading data from: ' + file_to_save)
    df = pd.read_csv(file_to_save)
    df = df.sort_values('date')

#Graphing data
#plt.figure(figsize = (19,9))
#plt.plot(range(df.shape[0]),(df['3. low']+df['2. high'])/2.0)
#plt.xticks(range(0,df.shape[0],500),df['date'].loc[::500],rotation=45)
#plt.xlabel('date',fontsize=18)
#plt.ylabel('Mid Price',fontsize=18)
#plt.show()

#Data sets
high = df.loc[:,'2. high'].to_numpy()
low = df.loc[:,'3. low'].to_numpy()
mid = (high+low)/2.0
midIndex =math.floor(len(mid)/2)

trainingData = mid[:midIndex]
testingData = mid[midIndex:]
print(trainingData)
print(testingData)

#Normalize data
scaler = MinMaxScaler()
trainingData = trainingData.reshape(-1,1)
testingData = testingData.reshape(-1,1)

#Train the Scaler with training data and smooth data
smoothing_window_size = 400 #chosen to have 4 windows in data. Here data size is 1950
for di in range(0,1600,smoothing_window_size):
    scaler.fit(trainingData[di:di+smoothing_window_size,:])
    trainingData[di:di+smoothing_window_size,:] = scaler.transform(trainingData[di:di+smoothing_window_size,:])

#normalize the last bit of remaining data
scaler.fit(trainingData[di+smoothing_window_size:,:])
trainingData[di+smoothing_window_size:,:] = scaler.transform(trainingData[di+smoothing_window_size:,:])

# Reshape both train and test data
trainingData = trainingData.reshape(-1)

# Normalize test data
testingData = scaler.transform(testingData).reshape(-1)

# Smoothing with exponential moving average smoothing, generate smoother curves
EMA = 0.0
gamma = 0.1
for ti in range(midIndex):
  EMA = gamma*trainingData[ti] + (1-gamma)*EMA
  trainingData[ti] = EMA
#print(trainingData)

all_mid_data = np.concatenate([trainingData,testingData],axis=0)
#print(all_mid_data)

#standard average
std_avg_prediction(df, trainingData, all_mid_data)


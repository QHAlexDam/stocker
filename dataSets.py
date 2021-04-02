from imports import *
#Data sets

def createDataSets(df, winSize, rangei, rangef):
    high = df.loc[:,'2. high'].to_numpy()
    low = df.loc[:,'3. low'].to_numpy()
    mid = (high+low)/2.0
    midIndex =math.floor(len(mid)/2)
    trainingData = mid[:midIndex]
    testingData = mid[midIndex:]

    #Normalize data
    scaler = MinMaxScaler()
    trainingData = trainingData.reshape(-1,1)
    testingData = testingData.reshape(-1,1)

    #Train the Scaler with training
    smoothing_window_size = winSize #chosen to have 4 windows in data. Here data size is 1950
    for di in range(rangei,rangef,smoothing_window_size):
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

    all_mid_data = np.concatenate([trainingData,testingData],axis=0)

    return (scaler, trainingData, testingData, all_mid_data)
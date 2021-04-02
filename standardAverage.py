from imports import *
#t+1 prediction via Standard Average

def std_avg_prediction(df, trainingData, all_mid_data):
    print("Prediction based on standard average")

    window_size = 10
    N = trainingData.size
    std_avg_predictions = []
    std_avg_x = []
    mse_errors = []

    for prediction_index in range(window_size, N):
        if prediction_index >= N:
            date = dt.datetime.strptime(k, '%Y=%m-%d').date() + dt.timedelta(days=1)
        else:
            date = df.loc[prediction_index, 'date']
        
        std_avg_predictions.append(np.mean(trainingData[prediction_index - window_size:prediction_index]))
        mse_errors.append((std_avg_predictions[-1] - trainingData[prediction_index])**2)
        std_avg_x.append(date)

    print('MSE error standard avg: %.5f'  %(0.5*np.mean(mse_errors)))

    #Visualisation
    plt.figure(figsize = (18,9))
    plt.plot(range(df.shape[0]),all_mid_data,color='b',label='True')
    plt.plot(range(window_size,N),std_avg_predictions,color='orange',label='Prediction')
    plt.xlabel('Date')
    plt.ylabel('Mid Price')
    plt.legend(fontsize=18)
    plt.show()

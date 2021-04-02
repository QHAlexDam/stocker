from imports import *

def stockToCSV(fileName, stockTicker):
    if not os.path.exists(fileName):
        data = getStockDaily(stockTicker)[0]
        data.to_csv(fileName)
        print('Data saved to: %s' %fileName)
        df = pd.read_csv(fileName)
        df = df.sort_values('date')
    else:
        print('Loading data from: ' + fileName)
        df = pd.read_csv(fileName)
        df = df.sort_values('date')
        
    return (df)
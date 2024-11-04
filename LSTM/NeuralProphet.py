import pandas as pd
from neuralprophet import NeuralProphet
from matplotlib import pyplot as plt
import pickle

data = pd.read_csv('data/PRU2_2018-09-01_2018-09-15_9464c9cda8dce80d71af4c0f7524355bEDITADO.csv', na_values=[' ', ''])

data['time_utc'] = pd.to_datetime(data['time_utc'], format='%Y-%m-%d %H:%M:%S')
data = data[data[' svid']==131]
# print(data.dtypes)
# data = data[:1000]
# print(data)
# data = data[:50]
data = data[['time_utc', ' s4']]
data.columns = ['ds', 'y']
data['y'] = data['y'].astype(float)
# data.dropna(inplace=True)
# data.reset_index(drop=True, inplace=True)
# plt.plot(data['ds'], data['y'])
# plt.show()

pd.set_option('display.max_rows', None)
print(data)
# model = NeuralProphet()
# model.fit(data, freq='min ', epochs=1)

# future = model.predict(model.make_future_dataframe(data, periods=500))
# # print(future)
# plot1 = model.plot(future)  
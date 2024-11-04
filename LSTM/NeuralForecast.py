from neuralforecast import NeuralForecast
from neuralforecast.auto import AutoLSTM
from typing import Union

import pandas as pd
import numpy as np
import torch
import ray

class WMAPE(torch.nn.Module):

    def __init__(self):
        super(WMAPE, self).__init__()
        self.outputsize_multiplier = 1
        self.output_names = [""]
        self.is_distribution_output = False

    def domain_map(self, y_hat: torch.Tensor):
        return y_hat.squeeze(-1)

    def __call__(
        self,
        y: torch.Tensor,
        y_hat: torch.Tensor,
        mask: Union[torch.Tensor, None] = None,
    ):
        if mask is None:
            mask = torch.ones_like(y_hat)

        num = mask * (y - y_hat).abs()
        den = mask * y.abs()
        return num.sum() / den.sum()

def wmape(y_true, y_pred):
    return np.abs(y_true - y_pred).sum() / np.abs(y_true).sum()

dtype_dict = {
    'time_utc': 'str',            
    ' svid': 'int',
    ' azim': 'int',        # Assuming 'azim' should be a float
    ' elev': 'int',        # Assuming 'elev' should be a float
    ' s4': 'float'            # Assuming 'y' should be a float
}

def data_gathering():
    # read the files and concatenate them in one DataFrame
    # data = pd.read_csv('data/PRU2_2018-09-01_2018-09-15_9464c9cda8dce80d71af4c0f7524355bEDITADO.csv', na_values=[' ', ''])
    # data2 = pd.read_csv('data/PRU2_2018-09-16_2018-09-30_0e3c656e91e97b0b76c2cdcf83a52854EDITADO.csv', na_values=[' ', ''])
    # data = pd.read_csv('data/PRU2_2018-10-01_2018-10-15_bb7dc5eebff60d3a4aa2ab4ccb5cfb87EDITADO.csv', na_values=[' ', ''], encoding='ascii')
    # data = pd.concat([data, data2, data3], ignore_index=True)
    data = pd.read_csv('data/a.csv', na_values=[' ', ''], encoding='ascii')
    
    # rename columns to satisfy neuralforecast's requirements
    data = data.rename(
        columns={'time_utc': 'ds',
                 ' s4': 'y',
                 ' svid': 'unique_id',
                 ' azim': 'azim',
                 ' elev': 'elev'})
    
    # Set the right type to each column and remove rows with NaN values
    data['ds'] = pd.to_datetime(data['ds'], format='%Y-%m-%d %H:%M:%S')
    data['y'] = data['y'].astype(float)
    # data['azim'] = pd.to_numeric(data['azim'], errors='coerce')
    data.dropna(inplace=True)
    data.reset_index(drop=True, inplace=True)
    data['azim'] = data['azim'].astype(int)
    data['elev'] = data['elev'].astype(int)
    # print(data)
    return data

ray.init(num_gpus=0)
data = data_gathering()

# split data between train and validation
# train = data.loc[data['ds']<'2018-10-15 00:00:00']
# valid = data.loc[data['ds']>='2018-10-15 00:00:00']
train = data.loc[data['ds']<'2019-01-16 00:23:00']
valid = data.loc[data['ds']>='2019-01-16 00:23:00']
print(train)
print('\n\n\n')
print(valid)

models = [AutoLSTM(h=2, 
                   num_samples=30, 
                   loss=WMAPE())]

model = NeuralForecast(models=models, freq='min')

model.fit(train)

# p = model.predict().reset_index()
# p = p.merge(valid[['ds','unique_id', 'y']], on=['ds', 'unique_id'], how='left')
# print(wmape(p['y'], p['AutoLSTM']))

# model.fit(train, val_size=30)

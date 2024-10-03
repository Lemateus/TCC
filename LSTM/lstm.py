import pandas as pd
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

data=yf.download('AAPL')[['Adj Close']]
data.reset_index(inplace=True)
data.drop('Date', axis=1, inplace=True)
print(data)
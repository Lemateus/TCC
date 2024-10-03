from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import cross_val_predict, cross_validate
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from src.get_data import get_data_normalized, get_data_normalized_under_sample, get_data, get_data_normalized_csv
from grid_search import svc_grid, RandomF_grid, decisionT_grid, MLP_grid
from sklearn.model_selection import StratifiedKFold
from grid_search import KN_grid, Ada_grid, xg_boost
from src.report import report
from sklearn.svm import SVC
import numpy as np
import os

def training():
    print('hjkda')
    data = get_data_normalized()
    # rng = np.random.RandomState(0)
    cross_val_strat = StratifiedKFold(n_splits=5, shuffle=True, random_state=32)
    clf = GradientBoostingClassifier(loss='exponential', max_features='log2')
    y_pred = cross_val_predict(clf, data.samples, data.s4, cv=cross_val_strat)
    report(y_pred, data.s4, "GradientBoostingClassifier(loss='exponential', max_features='log2')")

def test():
    data = get_data_normalized_csv('data/PRU2_2018-09-01_2018-09-15_9464c9cda8dce80d71af4c0f7524355bEDITADO.csv')
    print(len(data.samples), len(data.s4))
    data = get_data_normalized_csv('data/PRU2_2018-09-16_2018-09-30_0e3c656e91e97b0b76c2cdcf83a52854EDITADO.csv', data)
    print(len(data.samples), len(data.s4))
    cross_val_strat = StratifiedKFold(n_splits=5, shuffle=True, random_state=32)
    clf = MLPClassifier(activation='relu', learning_rate='invscaling', solver='adam', max_iter=400)
    y_pred = cross_val_predict(clf, data.samples, data.s4, cv=cross_val_strat)
    report(y_pred, data.s4, "MLPClassifier(activation='relu', learning_rate='invscaling', solver='adam', max_iter=400)")

def mult_files():
    directory = '/home/lemateus/TCC/cintilacao/data'
    
    data = None
    count = 3
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        data = get_data_normalized_csv(file_path, data)
        print(len(data.samples), len(data.s4))
        print(file_path)
        count -= 1
        if count == 0: break
    
    cross_val_strat = StratifiedKFold(n_splits=5, shuffle=True, random_state=32)
    clf = MLPClassifier(activation='relu', learning_rate='invscaling', solver='adam', max_iter=400)
    y_pred = cross_val_predict(clf, data.samples, data.s4, cv=cross_val_strat)
    report(y_pred, data.s4, "MLPClassifier(activation='relu', learning_rate='invscaling', solver='adam', max_iter=400)")


# KN_grid.mainFunction()
# xg_boost.mainFunction()
# RandomF_grid.mainFunction()
# decisionT_grid.mainFunction()
# MLP_grid.mainFunction()
# svc_grid.mainFunction()
# Ada_grid.mainFunction()

# training()
# test()
mult_files()
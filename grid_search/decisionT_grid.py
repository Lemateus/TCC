import time, math
import matplotlib.pyplot as plt
from datetime import datetime
from sklearn.utils import Bunch
from sklearn.model_selection import train_test_split
from sklearn import datasets, metrics, svm
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.experimental import enable_halving_search_cv  # noqa
from sklearn.model_selection import GridSearchCV, HalvingGridSearchCV
import pandas
from src.get_data import get_data_normalized_under_sample

def mainFunction():
    print('Decision Tree')
    param_grid = {
        'criterion': ['gini', 'entropy', 'log_loss'],
        'splitter': ['best', 'random'],
        'max_features': ['sqrt', 'log2', None]
    }

    data = get_data_normalized_under_sample()

    clf = DecisionTreeClassifier(class_weight='balanced')

    hgs = HalvingGridSearchCV(estimator=clf, param_grid=param_grid, factor=2)
    print(len(data.samples), len(data.s4))
    hgs.fit(data.samples, data.s4)

    print(hgs.best_params_)
    # print(hgs.best_score_)
    # print(hgs.best_estimator_)
    # print(hgs.best_index_)
    # print(hgs.cv_results_)
    # df = pandas.DataFrame(hgs.cv_results_)
    # print(df)
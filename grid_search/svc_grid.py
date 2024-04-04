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
    print('SVC')
    gammas = [1e-1, 1e-2, 1e-4, 1e-6, 1e-7]
    Cs = [1, 10, 100, 1e4]
    param_grid = {"gamma": gammas, "C": Cs}

    data = get_data_normalized_under_sample()

    rng = np.random.RandomState(0)
    clf = SVC(random_state=rng)

    hgs = HalvingGridSearchCV(estimator=clf, param_grid=param_grid, factor=2, random_state=rng)
    print(len(data.samples), len(data.s4))
    hgs.fit(data.samples, data.s4)

    print(hgs.best_params_)
    # print(hgs.best_score_)
    # print(hgs.best_estimator_)
    # print(hgs.best_index_)
    # print(hgs.cv_results_)
    # df = pandas.DataFrame(hgs.cv_results_)
    # print(df)
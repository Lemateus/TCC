from sklearn.model_selection import cross_val_predict
from src.get_data import get_data_normalized
from grid_search import svc_grid, RandomF_grid, decisionT_grid, MLP_grid
from grid_search import KN_grid, Ada_grid, xg_boost
from src.report import report
from sklearn.svm import SVC
import numpy as np

def training():
    print('hjkda')
    data = get_data_normalized()
    rng = np.random.RandomState(0)
    clf = SVC(C=10000.0, gamma=1e-06, random_state=np.random.RandomState(0))
    y_pred = cross_val_predict(clf, data.samples, data.s4, cv=5)
    report(y_pred, data.s4, 'SVC(C=10000.0, gamma=1e-06)')

KN_grid.mainFunction()
xg_boost.mainFunction()
RandomF_grid.mainFunction()
decisionT_grid.mainFunction()
MLP_grid.mainFunction()
svc_grid.mainFunction()
Ada_grid.mainFunction()

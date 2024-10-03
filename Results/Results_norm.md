# Best parameters

## SVC

`SVC(C=10000.0, gamma=1e-06, random_state=RandomState(MT19937) at 0x7F6150C3B940)`

## Random Forest

`RandomForestClassifier(bootstrap=False, class_weight='balanced')`

```
Classification report for classifier:
              precision    recall  f1-score   support

          -1       0.31      0.68      0.42      4737
           1       0.99      0.94      0.96    115325

    accuracy                           0.93    120062
   macro avg       0.65      0.81      0.69    120062
weighted avg       0.96      0.93      0.94    120062


Confusion matrix:
[[  3211   1526]
 [  7284 108041]]
report done
```

## Decision Tree

`DecisionTreeClassifier(criterion='entropy', max_features='sqrt', splitter='best')`

```
Classification report for classifier:
              precision    recall  f1-score   support

          -1       0.53      0.51      0.52      4691
           1       0.98      0.98      0.98    115371

    accuracy                           0.96    120062
   macro avg       0.75      0.75      0.75    120062
weighted avg       0.96      0.96      0.96    120062


Confusion matrix:
[[  2413   2278]
 [  2174 113197]]
report done
```


## MPL Classifier

`MLPClassifier(activation='relu', learning_rate='invscaling', solver='adam', max_iter=400)`

```
Classification report for classifier:
              precision    recall  f1-score   support

          -1       0.53      0.06      0.11      4674
           1       0.96      1.00      0.98    115388

    accuracy                           0.96    120062
   macro avg       0.75      0.53      0.54    120062
weighted avg       0.95      0.96      0.95    120062


Confusion matrix:
[[   279   4395]
 [   249 115139]]
report done
```

## Ada

* Without classifier especification:
    * `AdaBoostClassifier(algorithm='SAMME.R', random_state=None)`
```
Classification report for classifier:
              precision    recall  f1-score   support

          -1       0.40      0.09      0.15      4722
           1       0.96      0.99      0.98    115340

    accuracy                           0.96    120062
   macro avg       0.68      0.54      0.56    120062
weighted avg       0.94      0.96      0.95    120062


Confusion matrix:
[[   438   4284]
 [   655 114685]]
```
* With classifier
    * `AdaBoostClassifier(algorithm= 'SAMME', estimator= RandomForestClassifier(bootstrap=False, class_weight='balanced_subsample'), random_state=None)`

```
Classification report for classifier:
              precision    recall  f1-score   support

          -1       0.34      0.66      0.45      4696
           1       0.99      0.95      0.97    115366

    accuracy                           0.94    120062
   macro avg       0.66      0.80      0.71    120062
weighted avg       0.96      0.94      0.95    120062


Confusion matrix:
[[  3100   1596]
 [  6026 109340]]
```

## KNeighborsClassifier

`KNeighborsClassifier(algorithm='ball_tree', n_neighbors=2, weights='uniform')`

```
Classification report for classifier:
              precision    recall  f1-score   support

          -1       0.39      0.58      0.46      4660
           1       0.98      0.96      0.97    115402

    accuracy                           0.95    120062
   macro avg       0.68      0.77      0.72    120062
weighted avg       0.96      0.95      0.95    120062


Confusion matrix:
[[  2708   1952]
 [  4302 111100]]
```

## Gradient (Xg boost)

* `GradientBoostingClassifier(criterion='squared_error', loss='log_loss', max_features='log2', n_estimators=100)`

```
Classification report for classifier:
              precision    recall  f1-score   support

          -1       0.72      0.07      0.13      4730
           1       0.96      1.00      0.98    115332

    accuracy                           0.96    120062
   macro avg       0.84      0.54      0.56    120062
weighted avg       0.95      0.96      0.95    120062


Confusion matrix:
[[   344   4386]
 [   136 115196]]

```

With:
```
cross_val_strat = StratifiedKFold(n_splits=5, shuffle=True, random_state=32)
clf = GradientBoostingClassifier(criterion='squared_error', loss='log_loss', max_features='log2', n_estimators=100)
y_pred = cross_val_predict(clf, data.samples, data.s4, cv=cross_val_strat)

Classification report for classifier:
              precision    recall  f1-score   support

          -1       0.70      0.07      0.13     11758
           1       0.96      1.00      0.98    288395

    accuracy                           0.96    300153
   macro avg       0.83      0.54      0.56    300153
weighted avg       0.95      0.96      0.95    300153

Confusion matrix: GradientBoostingClassifier(criterion='squared_error', loss='log_loss', max_features='log2', n_estimators=100)
[[   854  10904]
 [   374 288021]]

```

```
Classification report for classifier:
              precision    recall  f1-score   support

          -1       0.69      0.05      0.10     11758
           1       0.96      1.00      0.98    288395

    accuracy                           0.96    300153
   macro avg       0.83      0.53      0.54    300153
weighted avg       0.95      0.96      0.95    300153


Confusion matrix: GradientBoostingClassifier(loss='exponential', max_features='log2')
[[   635  11123]
 [   279 288116]]
```

```
653488 653488
/home/lemateus/TCC/cintilacao/data/PRU2_2019-02-16_2019-02-28_1c2b60f47a77d9a49f22b3a82c8eab68EDITADO.csv
1022892 1022892
/home/lemateus/TCC/cintilacao/data/PRU2_2018-11-16_2018-11-30_7612d33b077fd2d54565df4a43a1a3c9EDITADO.csv
1790489 1790489
/home/lemateus/TCC/cintilacao/data/PRU2_2019-01-16_2019-01-31_5a011bc1d9ebd4a8c7e75c59d22f8487EDITADO.csv
Classification report for classifier:
              precision    recall  f1-score   support

          -1       0.57      0.03      0.06     12815
           1       0.99      1.00      1.00   1777674

    accuracy                           0.99   1790489
   macro avg       0.78      0.51      0.53   1790489
weighted avg       0.99      0.99      0.99   1790489


Confusion matrix: GradientBoostingClassifier(loss='exponential', max_features='log2')
[[    380   12435]
 [    287 1777387]]
```
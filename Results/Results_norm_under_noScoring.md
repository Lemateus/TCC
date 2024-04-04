# Best parameters without scoring='precision'

## KN
`KNeighborsClassifier(algorithm='kd_tree', n_neighbors=8, weights='uniform')`

```
Classification report for classifier:
              precision    recall  f1-score   support

          -1       0.85      0.97      0.91      4711
           1       0.72      0.30      0.43      1147

    accuracy                           0.84      5858
   macro avg       0.78      0.64      0.67      5858
weighted avg       0.82      0.84      0.81      5858


Confusion matrix:
[[4572  139]
 [ 798  349]]
```

## XG Boost

` GradientBoostingClassifier(criterion='squared_error', loss='log_loss', max_features='sqrt', n_estimators=100) `

```
Classification report for classifier:
              precision    recall  f1-score   support

          -1       0.90      0.99      0.94      4695
           1       0.96      0.55      0.70      1163

    accuracy                           0.91      5858
   macro avg       0.93      0.77      0.82      5858
weighted avg       0.91      0.91      0.90      5858


Confusion matrix:
[[4671   24]
 [ 523  640]]
```

## Random Forest
` RandomForestClassifier(bootstrap=True, class_weight='balanced_subsample')`

```
Classification report for classifier:
              precision    recall  f1-score   support

          -1       0.94      0.98      0.96      4696
           1       0.90      0.76      0.83      1162

    accuracy                           0.94      5858
   macro avg       0.92      0.87      0.89      5858
weighted avg       0.94      0.94      0.93      5858


Confusion matrix:
[[4599   97]
 [ 276  886]]
```

## Decision Tree

` DecisionTreeClassifier(criterion='gini', max_features='sqrt', splitter='best')`

```
Classification report for classifier:
              precision    recall  f1-score   support

          -1       0.94      0.97      0.96      4694
           1       0.86      0.76      0.81      1164

    accuracy                           0.93      5858
   macro avg       0.90      0.86      0.88      5858
weighted avg       0.93      0.93      0.93      5858


Confusion matrix:
[[4556  138]
 [ 283  881]]
```

## MLP

` MLPClassifier(activation='tanh', learning_rate='constant', solver='adam', max_iter=400) `

```
Classification report for classifier:
              precision    recall  f1-score   support

          -1       0.83      0.97      0.90      4663
           1       0.67      0.22      0.33      1195

    accuracy                           0.82      5858
   macro avg       0.75      0.60      0.62      5858
weighted avg       0.80      0.82      0.78      5858


Confusion matrix:
[[4534  129]
 [ 929  266]]
```

## SVC

`SVC(C=10000.0, gamma=1e-06)`
```
Classification report for classifier:
              precision    recall  f1-score   support

          -1       0.81      1.00      0.89      4735
           1       0.00      0.00      0.00      1123

    accuracy                           0.81      5858
   macro avg       0.40      0.50      0.45      5858
weighted avg       0.65      0.81      0.72      5858


Confusion matrix:
[[4735    0]
 [1123    0]]
```

## Ada

`AdaBoostClassifier(algorithm= 'SAMME', estimator= RandomForestClassifier(bootstrap=False, class_weight='balanced_subsample'), random_state=0)`

```
Classification report for classifier:
              precision    recall  f1-score   support

          -1       0.95      0.97      0.96      4699
           1       0.88      0.78      0.83      1159

    accuracy                           0.94      5858
   macro avg       0.91      0.88      0.90      5858
weighted avg       0.93      0.94      0.93      5858


Confusion matrix:
[[4576  123]
 [ 250  909]]
```

` AdaBoostClassifier(algorithm= 'SAMME', estimator= RandomForestClassifier(bootstrap=True, class_weight='balanced_subsample'), random_state=0) `

```
Classification report for classifier:
              precision    recall  f1-score   support

          -1       0.94      0.98      0.96      4665
           1       0.89      0.75      0.82      1193

    accuracy                           0.93      5858
   macro avg       0.92      0.86      0.89      5858
weighted avg       0.93      0.93      0.93      5858


Confusion matrix:
[[4557  108]
 [ 296  897]]
```
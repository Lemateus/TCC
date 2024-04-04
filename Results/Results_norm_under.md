# Best parameters

## Ada

` AdaBoostClassifier(algorithm= 'SAMME', estimator= RandomForestClassifier(bootstrap=False, class_weight='balanced_subsample'), random_state=None) `

```
Classification report for classifier:
              precision    recall  f1-score   support

          -1       0.96      0.97      0.96      4718
           1       0.88      0.82      0.84      1140

    accuracy                           0.94      5858
   macro avg       0.92      0.89      0.90      5858
weighted avg       0.94      0.94      0.94      5858


Confusion matrix:
[[4585  133]
 [ 209  931]]
```

## KN
` KNeighborsClassifier(algorithm='ball_tree', n_neighbors=2, weights='uniform') `

```
Classification report for classifier:
              precision    recall  f1-score   support

          -1       0.85      0.98      0.91      4682
           1       0.81      0.33      0.47      1176

    accuracy                           0.85      5858
   macro avg       0.83      0.66      0.69      5858
weighted avg       0.85      0.85      0.82      5858


Confusion matrix:
[[4589   93]
 [ 783  393]]

```

## XG Boost
` GradientBoostingClassifier(criterion='friedman_mse', loss='log_loss', max_features='sqrt', n_estimators=10) `


```
Classification report for classifier:
              precision    recall  f1-score   support

          -1       0.85      1.00      0.92      4746
           1       1.00      0.24      0.39      1112

    accuracy                           0.86      5858
   macro avg       0.92      0.62      0.65      5858
weighted avg       0.88      0.86      0.82      5858


Confusion matrix:
[[4746    0]
 [ 843  269]]
```

## Random Forest

` RandomForestClassifier(bootstrap=False, class_weight='balanced') `

```
Classification report for classifier:
              precision    recall  f1-score   support

          -1       0.94      0.96      0.95      4677
           1       0.84      0.76      0.80      1181

    accuracy                           0.92      5858
   macro avg       0.89      0.86      0.88      5858
weighted avg       0.92      0.92      0.92      5858


Confusion matrix:
[[4506  171]
 [ 278  903]]
```

## Decision Tree

` DecisionTreeClassifier(criterion='log_loss', max_features=None, splitter='best') `

```
Classification report for classifier:
              precision    recall  f1-score   support

          -1       0.94      0.97      0.95      4681
           1       0.87      0.75      0.80      1177

    accuracy                           0.93      5858
   macro avg       0.90      0.86      0.88      5858
weighted avg       0.92      0.93      0.92      5858


Confusion matrix:
[[4546  135]
 [ 297  880]]

```

import pandas as pd

data = {"A": [1, 1, 2, 2],
        "B": [1, 2, 3, 4],
        "C": [6, 7, 8, 9]}
data = pd.DataFrame(data)
print(data.head(2), '\n\n')
x = data.iloc[:, 2:3]
print(x)
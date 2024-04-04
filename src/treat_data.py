from sklearn.model_selection import train_test_split

def treat_data(data):
    X_train, X_test, y_train, y_test = train_test_split(
        data.samples, data.s4, test_size=0.4, shuffle=True
    )
    return X_train, X_test, y_train, y_test
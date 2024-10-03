from sklearn import metrics
import matplotlib.pyplot as plt

def report(predicted, s4_test, name):
    print(
    f"Classification report for classifier:\n"
    f"{metrics.classification_report(s4_test, predicted)}\n"
    )

    disp = metrics.ConfusionMatrixDisplay.from_predictions(s4_test, predicted)
    disp.figure_.suptitle(f"Confusion Matrix ({name})")
    print(f"Confusion matrix: {name}\n{disp.confusion_matrix}")
    plt.show()
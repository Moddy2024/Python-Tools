# CatBoost Classifier Example

"""
Catboost can  be installed by
!pip install catboost
if this model is not present  then you can run the above code for installation
"""

from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
from sklearn.metrics import plot_confusion_matrix
from sklearn.model_selection import train_test_split
from catboost import CatBoostClassifier


def main() -> None:

  """
    The Url for the algorithm
    https://catboost.ai/en/docs/concepts/python-reference_catboostclassifier
    Iris type dataset is used to demonstrate algorithm.
  """

  # Load Iris dataset
  iris = load_iris()

  # Split dataset into train and test data
  x = iris["data"]  # features
  y = iris["target"]
  x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.25)

  # XGBoost Classifier
  cbc = CatBoostClassifier()
  cbc.fit(x_train, y_train)

  # Display Confusion Matrix of Classifier
  # with both train and test sets
  plot_confusion_matrix(
        cbc,
        x_test,
        y_test,
        display_labels=iris["target_names"],
        cmap="inferno",
        normalize="true")
  plt.title("Normalized Confusion Matrix - IRIS Dataset")
  plt.show()


if __name__ == "__main__":
    main()
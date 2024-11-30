import numpy as np
from collections import Counter

def knn(x_train, y_train, x_test, y_test, k=5):
    # KNN Algorithm - From all the points, it selects the closes k points
    # Closes train and test points
    distances = euclidean_distance(x_train, x_test)
    neighbor = np.argsort(distances)[:k]
    neighbor_label = [y_train[i] for i in neighbor]

    return Counter(neighbor_label).most_common(1)[0][0]

    
def euclidean_distance(X_train, X_test):
    distances = []
    for x in X_train:
        distances = [np.sqrt((X_test - x) ** 2)]
    return distances
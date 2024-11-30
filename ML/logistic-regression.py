import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

X = np.array([[1], [2], [3], [4], [5], [6]])
y = np.array([0, 0, 0, 1, 1, 1])

model = LogisticRegression()
model.fit(X, y)

y_pred = model.predict(X)

acc = accuracy_score(y, y_pred)

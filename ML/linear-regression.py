import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

x = np.array([[1], [2], [3], [4], [5]])
y = np.array([1.2, 1.9, 3.1, 4.0, 5.1])

model = LinearRegression()
model.fit(x, y)

y_pred = model.predict(x)

score = model.score()
print(score)
mse = mean_squared_error(y, y_pred)
print(mse)

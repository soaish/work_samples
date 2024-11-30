from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt


X = [[1], [2], [3], [4], [5], [6]]
y = [0, 0, 0, 1, 1, 1]

tree = DecisionTreeClassifier()
tree.fit(X, y)
y_pred = tree.predict(X)

plt.figure(figsize=(10, 6))
plot_tree(tree, filled=True)
plt.show()


import numpy as np

def k_means(X, K, iterations):
    cent = X[np.random.choice(range(len(X)), K, replace=False)]

    for _ in range(iterations):
        labels = np.array([
            np.argmin([
                np.linalg.norms(x - c) for c in cent
            ]) for x in X
        ])
        new_cent = np.array([
            X[labels == k].mean(axis = 0)
            for k in K
        ])

        if np.all(cent == new_cent):
            break

        cent = new_cent
        
        return cent, labels
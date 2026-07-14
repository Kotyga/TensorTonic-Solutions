import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    X = np.asarray(X)
    shape = X.shape
    if len(shape) < 2:
        return None
    else:
        N, D = shape
        if N < 2:
            return None
        else:
            mean = X.mean(axis = 0)
            X_cent = X - mean
        
            return 1/(N-1) * X_cent.T @ X_cent
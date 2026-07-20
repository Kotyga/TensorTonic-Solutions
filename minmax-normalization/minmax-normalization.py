import numpy as np

def minmax_scale(X, axis=0, eps=1e-12):
    """
    Scale X to [0,1]. If 2D and axis=0 (default), scale per column.
    Return np.ndarray (float).
    """
    min_ = np.min(X, axis=axis, keepdims=True) 
    max_ = np.max(X, axis=axis, keepdims=True) 

    scal_X = (X - min_) / (max_ - min_ + eps)

    return scal_X
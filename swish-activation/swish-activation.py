import numpy as np

def sigma(x):
    return 1/(1 + np.exp(-x))

def swish(x):
    """
    Implement Swish activation function.
    """
    x = np.asarray(x, dtype=float)
    return x * sigma(x)
import numpy as np
from scipy import special
import math

def gelu(x):
    """
    Compute the Gaussian Error Linear Unit (exact version using erf).
    x: list or np.ndarray
    Return: np.ndarray of same shape (dtype=float)
    """
    correct = 2 ** -0.5
    x = np.asarray(x, dtype=float)
    return 0.5 * x * (1 + special.erf(x * correct))

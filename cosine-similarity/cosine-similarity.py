import numpy as np

def vec_len(x):
    return sum(x ** 2) ** 0.5

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    a = np.asarray(a)
    b = np.asarray(b)
    len_a = vec_len(a)
    len_b = vec_len(b)

    if len_a == 0 or len_b == 0:
        return 0
    else:
        return (a @ b) / (len_a * len_b)
    
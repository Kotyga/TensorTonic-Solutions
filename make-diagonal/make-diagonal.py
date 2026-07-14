import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    diagonal_elements = np.asarray(v)
    diag_matrix = np.diag(diagonal_elements)

    return diag_matrix

import numpy as np

def matrix_transpose(A):
    A_ = np.asarray(A)
    n, m = A_.shape
    B = np.zeros((m, n))
    for i in range(m):
        for j in range(n): 
            B[i][j] = A[j][i]
    return B
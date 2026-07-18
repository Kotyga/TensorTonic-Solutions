import numpy as np


def positional_encoding(seq_len, d_model, base=10000.0):
    """
    Return PE of shape (seq_len, d_model) using sin/cos formulation.
    Odd d_model -> last column is sin.
    """
    positions = np.arange(seq_len, dtype=np.float64)[:, np.newaxis]
    dimensions = np.arange(d_model)[np.newaxis, :]

    exponents = 2 * (dimensions // 2) / d_model
    angles = positions / np.power(base, exponents)

    return np.where(
        dimensions % 2 == 0,
        np.sin(angles),
        np.cos(angles),
    )
    
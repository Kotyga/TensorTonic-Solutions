import numpy as np

def positional_encoding(seq_length: int, d_model: int, base=10_000) -> np.ndarray:
    """
    Generate sinusoidal positional encodings.
    """
    positions = np.arange(seq_length, dtype=np.float64)[:, np.newaxis]
    dimensions = np.arange(d_model)[np.newaxis, :]

    exponents = 2 * (dimensions // 2) / d_model
    angles = positions / np.power(base, exponents)

    return np.where(
        dimensions % 2 == 0,
        np.sin(angles),
        np.cos(angles),
    )
import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    if sum(p) != 1:
        raise ValueError("sum(p) != 1")
        
    if len(p) != len(x):
        raise ValueError("len(p) != len(x)")

    else:
        x = np.asarray(x)
        p = np.asarray(p)

        return sum(x * p)

    

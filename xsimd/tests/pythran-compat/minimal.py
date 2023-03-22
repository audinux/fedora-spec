#pythran export minimal(float64[])
import numpy as np

def minimal(x):
    return np.sum(1. + x)

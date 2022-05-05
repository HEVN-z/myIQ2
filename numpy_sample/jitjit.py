from numba import jit, cuda
import numpy as np

@jit(nopython=True)
def add(a, b):
    return a + b
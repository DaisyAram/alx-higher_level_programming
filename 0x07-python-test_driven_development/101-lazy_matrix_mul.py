#!/usr/bin/python3
"""function that multiplies two matrices by using numpy"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """return mul of 2 matrices m_a and m_b"""

    return(np.matmul(m_a, m_b))

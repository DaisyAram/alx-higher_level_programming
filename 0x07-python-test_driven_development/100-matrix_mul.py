#!/usr/bin/python3
"""func that multiiplies two matrices"""


def matrix_mul(m_a, m_b):
    """mul two matrices
     Validate m_a"""
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not m_a:
        raise ValueError("m_a can't be empty")
    if not all(isinstance(element, (int, float)) for row in m_a for element in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    """Validate m_b"""
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if not m_b:
        raise ValueError("m_b can't be empty")
    if not all(isinstance(element, (int, float)) for row in m_b for element in row):
        raise TypeError("m_b should contain only integers or floats")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    """Check if m_a and m_b can be multiplied"""
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    """Perform the multiplication"""
    new_matrix = []
    for row in m_a:
        new_row = []
        for col in zip(*m_b):
            prod = sum(a * b for a, b in zip(row, col))
            new_row.append(prod)
        new_matrix.append(new_row)

    return new_matrix

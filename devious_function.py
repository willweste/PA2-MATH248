# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 13:25:03 2024

@author: kendall
"""


def f(x):
    import numpy as np
    first_part = (np.exp(2*x - 1) - (2*x**2) - 0.5)
    second_part = (np.cos(x) - np.exp(-1*x ** 2) + 1)
    third_part = (x**5 - (9 * x**4) - (x**3) + (17*x**2) - (8*x) - 8)

    answer = first_part * second_part * third_part
    return answer

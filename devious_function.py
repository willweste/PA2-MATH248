# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 13:25:03 2024

@author: kendall
"""


def devious_function(x):
    import numpy as np
    return (np.exp(2*x - 1) - (2*x**2) - (1/2)) * (np.cos(x) - np.exp(-1*x**2) + 1) * ((x**5) - (9*x**4) - (x**3) + (17*x**2) - (8*x) - 8)

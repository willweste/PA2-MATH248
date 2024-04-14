"""
This function returns a root using Newton's Method.
"""


def Newton_Method_ex(x_0, tol):
    import numpy as np

    max_itt = 1000
    x = np.zeros(max_itt+1)
    error = np.zeros(max_itt+1)

    error[1] = 10.0
    x[1] = x_0
    k = 1

    while (error[k] > tol) and (k < max_itt):
        x[k+1] = x[k] - f(x[k])/df(x[k])

        k = k+1
        error[k] = abs(x[k]-x[k-1])

    print('x[k]=', x[k])

    return x[k]


def f(x):
    import numpy as np
    val = (x**5 - (9*x**4) - x**3 + (17 * x**2) - 8*x - 8)

    return val


def df(x):
    import numpy as np
    val = ((5*x**4) - (36*x**3) - (3*x**2) + 34*x - 8)

    return val

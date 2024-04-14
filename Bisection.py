# -*- coding: utf-8 -*-
"""
This function returns a root using Bisection Method.
We assume that both f(a) and f(b) are nonzero and of opposite signs

"""


def bisection(a, b, tol1, tol2):
    import numpy as np

    max_itt = 1+int(np.ceil(np.log((b-a)/tol1)/np.log(2.0)))

    # print(max_itt)

    c = np.zeros(max_itt+1)
    error = np.zeros(max_itt+1)

    error[1] = 10.0

    k = 1

    c[1] = (a + b)/2.0

    fa = f(a)
    fc = f(c[1])

    while error[k] > tol1 and k < max_itt and abs(fc) > tol2:

        if fa*fc < 0.0:
            b = c[k]
        else:
            a = c[k]
            fa = f(a)

        c[k+1] = (a + b)/2.0
        fc = f(c[k+1])

        # print('error[', k, ']=', error[k])

        error[k+1] = abs(c[k+1]-c[k])

        k = k+1

    # print('error[',k,']=',error[k],'\n')

    print('c[', k, ']=', c[k])

    return c[k]  # ,error


def f(x):
    import numpy as np
    val = (x**5 - (9 * x**4) - (x**3) + (17*x**2) - (8*x) - 8)

    return val


def bisection2(a, b, tol1, tol2):
    import numpy as np

    max_itt = 1+int(np.ceil(np.log((b-a)/tol1)/np.log(2.0)))

    # print(max_itt)

    c = np.zeros(max_itt+1)
    error = np.zeros(max_itt+1)

    error[1] = 10.0

    k = 1

    c[1] = (a + b)/2.0

    fa = f2(a)
    fc = f2(c[1])

    while error[k] > tol1 and k < max_itt and abs(fc) > tol2:

        if fa*fc < 0.0:
            b = c[k]
        else:
            a = c[k]
            fa = f2(a)

        c[k+1] = (a + b)/2.0
        fc = f2(c[k+1])

        # print('error[', k, ']=', error[k])

        error[k+1] = abs(c[k+1]-c[k])

        k = k+1

    # print('error[',k,']=',error[k],'\n')

    print('c[', k, ']=', c[k])

    return c[k]  # ,error


def f2(x):
    import numpy as np
    val = (np.cos(x) - np.exp(-1*x**2) + 1)

    return val

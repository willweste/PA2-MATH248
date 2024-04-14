"""
Programing Assignment 2 - Superman
Math 248 Section 2
Members: Josh Bowers, Kendall Coleman, Jamie Fuller, William Westerkamp, and Fralin Widener

@author: Kendall Coleman
"""

# imports
import numpy as np
import openpyxl as op
from openpyxl import Workbook
from Altered_Newtons_Method import Altered_Newton_Method
from Fixed_point_iteration import fixedPointIteration1
from Fixed_point_iteration import fixedPointIteration2
from Halley_Method import Halley_Method
from Olvers_Method import Olver_Method
from Bisection import bisection
from Bisection import bisection2
from newton_method_ex import Newton_Method_ex
from devious_function import f

# create excel file
workbook = Workbook()
workbook.save(filename="Lex_will_Perish.xlsx")
worksheet = workbook.worksheets[0]

# hard coded values to run through methods
tol = 10**-14
b_tol = 1e-14
"""
halley_method_number = 9 # or 10
#fixed_point_number = any values
olver_method_number = 2
#altered_newton_number =
"""

# run each value through newton's method and a fixed point method

# converges to +-1.38750710558261
if (Newton_Method_ex(-2, tol) == Olver_Method(-2, tol)):
    print("yay")

# converges to +-3.15145284329665
if (Newton_Method_ex(4, tol) == (np.floor(Halley_Method(5, 10**-14) * 10**14) / 10**14)):
    print("please work")

# run each value through bisection method and a fixed point method

# converges to +-0.51042934281782
if (bisection(-1, 0, b_tol, b_tol) == (np.floor(fixedPointIteration1(-1, 10**-14) * 10**14) / 10**14)):
    print("test")

# converges to +-8.91069640296029
if (bisection(7, 9, b_tol, b_tol) == (np.floor(Halley_Method(9, 10**-14) * 10**14) / 10**14)):
    print("8.91069640296029")
    root_somenumber = bisection(7, 9, b_tol, b_tol)

# converges to +-3.13108083857006
if (bisection2(3, 3.13, b_tol, b_tol) == (np.floor(fixedPointIteration2(3, 10**-14) * 10**14) / 10**14)):
    print("this works")

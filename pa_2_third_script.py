"""
Programing Assignment 2 - Superman
Math 248 Section 2
Members: Josh Bowers, Kendall Coleman, Jamie Fuller, William Westerkamp, and Fralin Widener

@author: Kendall Coleman
"""
# imports
from openpyxl import Workbook
from openpyxl import load_workbook
from pa_2_first_script import lock_box_codes
import numpy as np
import openpyxl as op


def directions_string(x, y):
    """
    Converts x and y into miles and computes directions from the Eiffel Tower

    Parameters
    ----------
    x : float
        X-coordinate of the Kryptonite location.
    y : float
        Y-coordinate of the Kryptonite Location.

    Returns
    -------
    str
        Directions string.

    """
    # set values
    x_miles = x * 100
    y_miles = y * 100
    x_direction = ""
    y_direction = ""

    # calculate directions
    if x_miles >= 0:
        x_direction = "East"
    else:
        x_direction = "West"
    if y_miles >= 0:
        y_direction = "North"
    else:
        y_direction = "South"

    return f"(x, y) = ({x}, {y}).\nGo {x_miles} {x_direction} and {y_miles} {y_direction}."


# load in Lex_will_Perish

end_of_Lex = load_workbook("end_of_Lex.xlsx")
Lex_sheet = end_of_Lex.worksheets[0]

root_array = []
bs_array = []
sc_array = []

for row in Lex_sheet.iter_rows(values_only=True):
    root_array.append(row[0])
    bs_array.append(row[1])
    sc_array.append(row[2])

# calculate y-coordinates
y_array = []

for root_index, root in enumerate(root_array):
    # compute y-coordinate
    y_cord = np.log(bs_array[root_index] - sc_array[root_index])
    # store y-coordinate
    y_array.append(y_cord)
    # print out coordinates
    print(directions_string(root_array[root_index], y_array[root_index]))
    print(f"The secret lock box comination is {lock_box_codes[root_index]}.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

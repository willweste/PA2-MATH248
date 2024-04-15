"""
Programing Assignment 2 - Superman
Math 248 Section 2
Members: Josh Bowers, Kendall Coleman, Jamie Fuller, William Westerkamp, and Fralin Widener

@author: Kendall Coleman
"""
# imports
from openpyxl import Workbook
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

    return f"(x, y) = ({x}, {y}). Go {x_miles} {x_direction} and {y_miles} {y_direction}."


end_of_Lex = op.load_workbook("end_of_Lex.xlsx")
end_of_Lex_sheet = end_of_Lex.worksheets[0]

root_array = []
bs_array = []
sc_array = []

for column in end_of_Lex_sheet.iter_cols():
    column_title = column[0].value
    # check column name
    if column_title == "r_k":
        for cell in column:
            root_array.append(cell.value)
    elif column_title == "bs_k":
        for cell in column:
            bs_array.append(cell.value)
    elif column_title == "sc_k":
        for cell in column:
            sc_array.append(cell.value)

# calculate y-coordinates
y_array = []
root_index = 0
for root in root_array:
    # compute y-coordinate

    # store y-coordinate

    # print out coordinates
    directions_string(root_array[root_index], y_array[root_index])
    print(f"The secret lock box comination is {lock_box_codes[root_index]}")

    # increase counter
    root_index = root_index + 1

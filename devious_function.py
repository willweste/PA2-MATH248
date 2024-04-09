# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 13:25:03 2024

@author: kendall & Josh
"""

#%% Full Function
import numpy as np
import matplotlib.pyplot as plt
def devious_function(x):
    return (np.exp(2*x - 1) - (2*x**2) - (1/2)) * (np.cos(x) - np.exp(-1*x**2) + 1) * ((x**5) - (9*x**4) - (x**3) + (17*x**2) - 8*x - 8)

# with np.linspace we can change the interval of the plot to better visualize the function
# you can change the first two terms in the linspace above to view a certain interval
x = np.linspace(-10, 10, 1000)
# for example if you would like to view the interval [-1,1] then you would enter np.linspace(-1, 1, 1000)
# the 1000 at the end just allows for the represntation of the function to be more accurate
y = devious_function(x)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.grid(True, which='both')
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')

plt.show()

#%% Devious Function is split into 3 seperate functions
#%% This is done so that the root assumption process is quicker and easier as it allows the user to visualize each major portion of the function
#%% This also allows the user to create plots in which they can visualize different intervals of the functions to find potential roots

#%% Root Function 1
import numpy as np
import matplotlib.pyplot as plt
def Root_1_Function(x):
    return (np.exp(2*x - 1) - (2*x**2) - (1/2)) 

x = np.linspace(-10, 10, 1000)
y = Root_1_Function(x)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.grid(True, which='both')
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')

plt.show()

#%% Root Function 2
import numpy as np
import matplotlib.pyplot as plt
def Root_2_Function(x):
    return (np.cos(x) - np.exp(-1*x**2) + 1) 

x = np.linspace(-10, 10, 1000)
y = Root_2_Function(x)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.grid(True, which='both')
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')

plt.show()

#%% Root Function 3
import numpy as np
import matplotlib.pyplot as plt
def Root_3_Function(x):
    return ((x**5) - (9*x**4) - (x**3) + (17*x**2) - 8*x - 8)

x = np.linspace(-10, 10, 1000)
y = Root_3_Function(x)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.grid(True, which='both')
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')

plt.show()

# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 21:47:39 2024

@author: joshb
"""

import numpy as np
# Defining the Nonlinear Function
def f(x):
    return #insert function here

# Implementing the Secant Method
def secant_method(x0, x1, tol):
    print("\n\n*** SECANT METHOD IMPLEMENTATION ***")
    
    max_itt = 1000
    x = np.zeros(max_itt+1)
    error = np.zeros(max_itt+1)
    
    error[1] = 10.0
    x[1] = x0
    x[2] = x1
    k = 1
    
    while (error[k] > tol) and (k < max_itt) :
        x[k+2] = x[k+1] - (x[k+1]-x[k])*f(x[k+1])/(f(x[k+1])-f(x[k]))
        
        print('error(',k,')=',error[k])
        
        k = k+1
        
        error[k] = abs(x[k+1]-x[k])  
   
     
    print('error[',k,']=',error[k],'\n')
   
    print('k=',k)
    print('x[k]=',x[k])
   
    return x,error


# Input Section
x0 = float(input("Enter First Guess: "))
x1 = float(input("Enter Second Guess: "))
e = float(input("Tolerable Error: "))

# Starting the Secant Method
secant_method(x0, x1, e)

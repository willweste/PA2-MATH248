# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 14:38:16 2024

@author: joshb
"""

import numpy as np


def f(x):
    return  (np.cos(x) - np.exp(-1*x**2) + 1) 

def g(x):
    return  np.arccos(np.exp(-1*x**2) - 1) 

# Implementing Fixed Point Iteration Method
def fixedPointIteration(x0, tol):
    print("\n\n*** FIXED POINT ITERATION ***")
    
    max_itt = 1000
    x = np.zeros(max_itt+1)
    error = np.zeros(max_itt+1)
    
    error[1] = 10.0
    x[1] = x0
    k = 1
    

    while (error[k] > tol) and (k < max_itt) :
        x[k+1] = g(x0)
        print(f"Iteration-{k}, x[k] = {x[k]:.16f} and f(x[k]) = {f(x[k]):.16f}")
        x0 = x[k+1]
        
        print('error(',k,')=',error[k])
        
        k = k+1

        error[k] = abs(x[k]-x[k-1]) 

    print('error[',k,']=',error[k],'\n')
    
    print('k=',k)
    print('x[k]=',x[k])
   
    return x,error
        

# Input Section
x0 = float(input("Enter Guess: "))
tol = float(input("Tolerable Error: "))

# Starting Fixed Point Iteration Method
fixedPointIteration(x0, tol)
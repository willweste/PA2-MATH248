# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 19:18:34 2024

@author: joshb
"""
import numpy as np

def f(x):
    return #((x**5) - (9*x**4) - (x**3) + (17*x**2) - 8*x - 8)

def df(x):
    return #((5*x**4) - (36*x**3) - (3*x**2) + (34*x) - 8)

def df_2(x):
    return #((20*x**3) - (108*x**2) - (6*x) + 34)


def Halley_Method(x0,tol):
      import numpy as np
            
      max_itt = 1000
      x = np.zeros(max_itt+1)
      error = np.zeros(max_itt+1)
      
      
      error[1] = 10.0
      x[1] = x0
      k = 1
      
      
      while (error[k] > tol) and (k < max_itt) :
           x[k+1] = x[k] - (2 * f(x[k]) * df(x[k]))/(2*((df(x[k])**2) - f(x[k]) * df_2(x[k])))
                              
           print('error(',k,')=',error[k])
           k = k+1
           error[k] = abs(x[k]-x[k-1])  
      
        
      print('error[',k,']=',error[k],'\n')
      
      print('k=',k)
      print('x[k]=',x[k])
      
      return x,error
  
    
x0 = float(input("Enter First Initial Guess: "))
tol = float(input("Enter the Tolerance: "))

Halley_Method(x0,tol)
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 16:11:36 2024

@author: joshb
"""
import numpy as np

def f(x):
    return (np.cos(x) - np.exp(-1*x**2) + 1)

def df(x):
    return ((2*x*np.exp(-1*x**2)) - np.sin(x))

def df_2(x):
    return (((-4*x**2)*np.exp(-1*x**2)) + (2*np.exp(-1*x**2)) - np.cos(x))


def Olver_Method(x0,tol):
      import numpy as np
            
      max_itt = 1000
      x = np.zeros(max_itt+1)
      error = np.zeros(max_itt+1)
      
      
      error[1] = 10.0
      x[1] = x0
      k = 1
      
      
      while (error[k] > tol) and (k < max_itt) :
           x[k+1] = x[k] - (f(x[k])/df(x[k])) - (1/2)*(((f(x[k]))**2)*df_2(x[k]))/((df(x[k]))**3)
                              
           print('error(',k,')=',error[k])
           k = k+1
           error[k] = abs(x[k]-x[k-1])  
      
        
      print('error[',k,']=',error[k],'\n')
      
      print('k=',k)
      print('x[k]=',x[k])
      
      return x,error
  
    
x0 = float(input("Enter First Initial Guess: "))
tol = float(input("Enter the Tolerance: "))

Olver_Method(x0,tol)


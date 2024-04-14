# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 18:57:10 2024

@author: joshb
"""

# altered Newtons method

def Altered_Newton_Method(x_0,tol):
      import numpy as np
            
      max_itt = 1000
      x = np.zeros(max_itt+1)
      error = np.zeros(max_itt+1)
      
      
      error[1] = 10.0
      x[1] = x_0
      k = 1
            
      while (error[k] > tol) and (k < max_itt) :
           x[k+1] = x[k] - df_2(x[k])/df_3(x[k])
                              
           print('error(',k,')=',error[k])
           k = k+1
           error[k] = abs(x[k]-x[k-1])  
      
        
      print('error[',k,']=',error[k],'\n')
      
      print('k=',k)
      print('x[k]=',x[k])
      
      return x,error
      
      
      
 
 
def df_2(x):
    #
    import numpy as np
    val = 4*np.exp(2*x - 1) - 4
    
    return val

 
def df_3(x):
    import numpy as np
    val = 8*np.exp(2*x - 1)
    
    return val

x_0 = float(input("Enter First Initial Guess: "))
tol = float(input("Enter the Tolerance: "))

Altered_Newton_Method(x_0,tol)
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 16:04:15 2024

@author: joshb
"""
#%% Functions
import numpy as np


def f(x):
    return ((x**5) - (9*x**4) - (x**3) + (17*x**2) - 8*x - 8) 


def g(x):
    return 8/(x**4 - 9*x**3 - x**2 + 17*x - 8)

def df(x):
    return ((5*x**4) - (36*x**3) - (3*x**2) + (34*x) - 8)

def df_2(x):
    return ((20*x**3) - (108*x**2) - (6*x) + 34)

#%% fixedPointIteration for ((x**5) - (9*x**4) - (x**3) + (17*x**2) - 8*x - 8)


# Implementing Fixed Point Iteration Method
def fixedPointIteration(x0, tol):
    print("\n\n*** FIXED POINT ITERATION ***")
    
    max_itt = 1000
    x = np.zeros(max_itt+1)
    error = np.zeros(max_itt+1)
    
    error[1] = 10.0
    x[1] = x0
    k = 1
    
    flag = 1

    while (error[k] > tol) and (k < max_itt) :
        x[k+1] = g(x0)
        print(f"Iteration-{k}, x[k] = {x[k]:.16f} and f(x[k]) = {f(x[k]):.16f}")
        x0 = x[k+1]
        k = k+1

        if k > max_itt:
            flag = 0
            break

        error[k] = abs(f(x[k])) > tol
                 
    if flag == 1:
        print(f"\nRequired root is: {x[k]:.16f}")
    else:
        print("\nNot Convergent.")

# Input Section
#x0 = float(input("Enter Guess: "))
#tol = float(input("Tolerable Error: "))

# Starting Fixed Point Iteration Method
fixedPointIteration(10, 1e-14)

#%% Halley's Method for ((x**5) - (9*x**4) - (x**3) + (17*x**2) - 8*x - 8)



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
  
    
#x0 = float(input("Enter First Initial Guess: "))
#tol = float(input("Enter the Tolerance: "))

Halley_Method(10,1e-14)

#%% Olver's Method for ((x**5) - (9*x**4) - (x**3) + (17*x**2) - 8*x - 8)


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
  
    
#x0 = float(input("Enter First Initial Guess: "))
#tol = float(input("Enter the Tolerance: "))

Olver_Method(-2, 1e-14)
#%% Newton's Method for ((x**5) - (9*x**4) - (x**3) + (17*x**2) - 8*x - 8)

def Newton_Method(x_0,tol):
      import numpy as np
            
      max_itt = 1000
      x = np.zeros(max_itt+1)
      error = np.zeros(max_itt+1)
      
      
      error[1] = 10.0
      x[1] = x_0
      k = 1
            
      while (error[k] > tol) and (k < max_itt) :
           x[k+1] = x[k] - f(x[k])/df(x[k])
                              
           print('error(',k,')=',error[k])
           k = k+1
           error[k] = abs(x[k]-x[k-1])  
      
        
      print('error[',k,']=',error[k],'\n')
      
      print('k=',k)
      print('x[k]=',x[k])
      
      return x,error
      
      

#x_0 = float(input("Enter First Initial Guess: "))
#tol = float(input("Enter the Tolerance: "))

Newton_Method(9,1e-14)
Newton_Method(-0.2,1e-14)
Newton_Method(-2,1e-14)
#%% Bisection Method for ((x**5) - (9*x**4) - (x**3) + (17*x**2) - 8*x - 8)

def bisection(a,b,tol1,tol2):
      import numpy as np
            
      max_itt = 1+int(np.ceil(np.log((b-a)/tol1)/np.log(2.0)))
      
      print(max_itt)
      
      
      c = np.zeros(max_itt+1)
      error = np.zeros(max_itt+1)
      
      error[1] = 10.0
      
     
      
      k = 1
      
      c[1]= (a + b)/2.0 
      
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
                  
           print('error[',k,']=',error[k])
           
                    
           error[k+1] = abs(c[k+1]-c[k])  
           
           k = k+1
        
      
      print('error[',k,']=',error[k],'\n')
      
      print('c[',k,']=',c[k])
      
      return c,error
      

 
#a = float(input("Enter First Initial Guess: "))
#b = float(input("Enter Second Initial Guess: "))
#tol1 = float(input("Enter the Tolerance: "))
#tol2 = float(input("Enter the Tolerance: "))

bisection(-2,-1,1e-14,1e-14)
bisection(-1,0,1e-14,1e-14)
bisection(7,9,1e-14,1e-14)

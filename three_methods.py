"""
Created on Tuesday Apr  9

@author: William
"""

import numpy as np
from devious_function import devious_function

def newton(f, x0, tol=1e-14, max_iter=100):
    """
    Newton's method for finding roots of a function f.

    Parameters:
    - f: The function to find the roots of.
    - x0: The initial guess for the root.
    - tol: The tolerance for convergence (default: 1e-14).
    - max_iter: The maximum number of iterations (default: 100).

    Returns:
    - The root of the function f.

    Raises:
    - RuntimeError: If the method fails to converge after max_iter iterations.
    """
    x = x0
    for i in range(max_iter):
        fx = f(x)
        if abs(fx) < tol:
            return x
        df = derivative_approximation(x)  # Approximate derivative using central difference
        if abs(df) < 1e-8:
            raise RuntimeError(f"Derivative is close to zero. Unable to proceed.")
        x = x - fx/df  # Update x using Newton's formula
    raise RuntimeError(f"Failed to converge after {max_iter} iterations")

def fixed_point(g, x0, tol=1e-14, max_iter=100):
    """
    Fixed-point iteration method for finding roots of a function f.

    Parameters:
    - g: The fixed-point function g(x) = x - f(x).
    - x0: The initial guess for the root.
    - tol: The tolerance for convergence (default: 1e-14).
    - max_iter: The maximum number of iterations (default: 100).

    Returns:
    - The root of the function f.

    Raises:
    - RuntimeError: If the method fails to converge after max_iter iterations.
    """
    x = x0
    for i in range(max_iter):
        x_new = g(x)
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    raise RuntimeError(f"Failed to converge after {max_iter} iterations")

def bisection(f, a, b, tol=1e-14, max_iter=100):
    """
    Bisection method for finding roots of a function f.

    Parameters:
    - f: The function to find the roots of.
    - a: The left endpoint of the interval.
    - b: The right endpoint of the interval.
    - tol: The tolerance for convergence (default: 1e-14).
    - max_iter: The maximum number of iterations (default: 100).

    Returns:
    - The root of the function f.

    Raises:
    - ValueError: If f(a) and f(b) have the same sign.
    - RuntimeError: If the method fails to converge after max_iter iterations.
    """
    if f(a)*f(b) >= 0:
        raise ValueError("f(a) and f(b) must have opposite signs")
    for i in range(max_iter):
        c = (a + b)/2  # Bisect the interval
        if f(c) == 0 or (b-a)/2 < tol:
            return c
        if f(c)*f(a) < 0:
            b = c  # Update the right endpoint
        else:
            a = c  # Update the left endpoint
    raise RuntimeError(f"Failed to converge after {max_iter} iterations")

def find_roots():
    """
    Find the roots of the devious function using Newton's method, fixed-point iteration, and bisection method.

    Returns:
    - A list of the roots found by the three methods.
    """
    newton_guesses = [-9.5, -7.5, -5.5, -3.5, -1.5, 0.5, 2.5, 4.5, 6.5, 8.5]  # Initial guesses for Newton's method
    fixed_point_gs = [
        lambda x: x - devious_function(x) / (derivative_approximation(x) + 1e-8),  # Fixed-point function for root near -9.5
        lambda x: x - devious_function(x) / (derivative_approximation(x) + 1e-8),  # Fixed-point function for root near -7.5
        lambda x: x - devious_function(x) / (derivative_approximation(x) + 1e-8),  # Fixed-point function for root near -5.5
        lambda x: x - devious_function(x) / (derivative_approximation(x) + 1e-8),  # Fixed-point function for root near -3.5
        lambda x: x - devious_function(x) / (derivative_approximation(x) + 1e-8),  # Fixed-point function for root near -1.5
        lambda x: x - devious_function(x) / (derivative_approximation(x) + 1e-8),  # Fixed-point function for root near 0.5
        lambda x: x - devious_function(x) / (derivative_approximation(x) + 1e-8),  # Fixed-point function for root near 2.5
        lambda x: x - devious_function(x) / (derivative_approximation(x) + 1e-8),  # Fixed-point function for root near 4.5
        lambda x: x - devious_function(x) / (derivative_approximation(x) + 1e-8),  # Fixed-point function for root near 6.5
        lambda x: x - devious_function(x) / (derivative_approximation(x) + 1e-8),  # Fixed-point function for root near 8.5
    ]
    bisection_intervals = [
        (-10, -9), (-8, -7), (-6, -5), (-4, -3), (-2, -1),
        (0, 1), (2, 3), (4, 5), (6, 7), (8, 9)
    ]  # Intervals for bisection method

    roots = []  # List to store the roots found

    # Find roots using Newton's method
    for x0 in newton_guesses:
        try:
            root = newton(devious_function, x0)
            roots.append(root)
            print(f"Newton's method converged to {root:.14f} for initial guess {x0}")
        except RuntimeError as e:
            print(f"Newton's method: {e} for initial guess {x0}")

    # Find roots using fixed-point iteration
    for i, g in enumerate(fixed_point_gs, start=1):
        try:
            root = fixed_point(g, newton_guesses[i-1])
            roots.append(root)
            print(f"Fixed-point iteration {i} converged to {root:.14f}")
        except RuntimeError as e:
            print(f"Fixed-point iteration {i}: {e}")

    # Find roots using bisection method
    for i, (a, b) in enumerate(bisection_intervals, start=1):
        try:
            root = bisection(devious_function, a, b)
            roots.append(root)
            print(f"Bisection method converged to {root:.14f} for interval [{a}, {b}]")
        except (ValueError, RuntimeError) as e:
            print(f"Bisection method: {e} for interval [{a}, {b}]")

    roots = sorted(list(set(roots)))  # Remove duplicate roots and sort the list
    return roots

def derivative_approximation(x, h=1e-8):
    """
    Approximate the derivative of the devious function at a point x using the central difference formula.

    Parameters:
    - x: The point at which to approximate the derivative.
    - h: The step size for the central difference formula (default: 1e-8).

    Returns:
    - The approximate derivative of the devious function at x.
    """
    return (devious_function(x + h) - devious_function(x - h)) / (2 * h)

if __name__ == "__main__":
    roots = find_roots()
    print(f"\nFinal roots: {[f'{root:.14f}' for root in roots]}")
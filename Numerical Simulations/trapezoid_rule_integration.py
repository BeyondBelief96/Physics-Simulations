import numpy as np
from numpy.linalg import *
from numpy import sin, pi

# Define constants and variables
a = 0.0  # Start point for integration
b = pi/2.0  # End point for integration
n = 100  # number of steps


# Define function to integrate
def f(x): return x*sin(x)


# Defining trapezoid rule algorithm
def trapezoid_rule(f, a, b, n):
    h = (b - a) / n  # step size (Equally-Spaced)
    # Calculate first term in summation
    Sum = 0.5*(f(a) + f(b))

    # loop to calculate rest of sum (range does not include n)
    for i in range(1, n):
        Sum += f(a + i*h)  # calculates ith term in summation at x = a + i*h
    Integral = h * Sum
    print('Integral = ', Integral)


trapezoid_rule(f, a, b, n)

import numpy as np
from numpy import sin, cos, pi

# Define constants and variables
a = 0.0  # Start point for integration
b = pi/2.0  # End point for integration
n = 100  # number of steps


# Define function to integrate
def f(x): return x*sin(x)


# defining Simpson's Rule Algorithm
def simpsons_rule(f, a, b, n):
    h = (b - a) / n
    # Calculate first term in summation
    Sum = f(a) + f(b)

    # loop to calculate rest of sum (range does not include n)
    for i in range(1, n):
        if(i % 2 == 0):
            Sum += 2*f(a + i*h)
        else:
            Sum += 4*f(a + i*h)

    Integral = h/3.0 * Sum
    print('Integral = ', Integral)


simpsons_rule(f, a, b, n)

import numpy as np
from matplotlib import pyplot as plt
from numpy import sin, cos, pi


# Defining function to return a general complex exponential of a given angular frequency w, amplitude C, exponential constant r, and phase theta
def complex_exponential(t, w, c, r, theta):
    return np.abs(c)*np.exp(r*t)*cos(w*t + theta) + 1j*abs(c)*np.exp(r*t)*sin(w*t + theta)


# Defining function to plot
def f(t):
    return complex_exponential(t, pi/2, 1, 0.1, pi)


y = []  # Array to store y values in

# Array of time values to calculate y values of function f(t)
time = np.arange(0, 30, 0.1)

# Loop to calculate f(t) for all values in time array
for t in time:
    y.append(f(t))

# Plotting function
plt.plot(time, y)
plt.show()

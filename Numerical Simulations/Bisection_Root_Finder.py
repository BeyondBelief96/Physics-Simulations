import numpy as np
from numpy import sin, cos, pi
from numpy.core.fromnumeric import size
from matplotlib import pyplot as plt

E = []
Y = []

# Define function to find roots for


def f(x):
    return np.sqrt(10 - x)*np.tan(np.sqrt(10 - x))


def bisection_algorithm(x_negative, x_positve, N, error):
    for i in range(N):
        x = (x_positve + x_negative) / 2.0

        if f(x_positve) * f(x) > 0:  # This tests whether we've crossed a zero
            x_positve = x
        else:
            x_negative = x
        if abs(f(x)) < error:
            break
    return x


zero = bisection_algorithm(0, 8, 100, 1e-6)
E = np.arange(0, 50, 0.1)

for i in E:
    Y.append(f(i))


plt.plot(E, Y)
print('Function has zero at x = ', zero)
plt.show()

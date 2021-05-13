import numpy as np
from matplotlib import pyplot as plt
from math import sin, cos, pi

# Setup constants and variables
c1 = 1.0
c2 = 0.0
dt = 0.01
time = np.arange(0.0, 2.5, dt)
y = 0
x = 0

Y = []
X = []


# time stepping solution
for t in time:
    x = c1*sin(t)**2
    y = c1*t - (c1/2)*sin(2*t) - c2
    Y.append(y)
    X.append(x)

# plotting results
# swapping y and x to "flip" graph to orient it in the brachistocrhone problem
plt.plot(X, Y)
plt.legend(['y(x)'], loc='lower right')
plt.show()

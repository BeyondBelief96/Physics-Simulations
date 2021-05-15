import numpy as np
from numpy import sin, cos, pi
from matplotlib import pyplot as plt


n = np.arange(0, 100, 1)
y = []


def f(t):
    return cos(8*pi*t/31)


for t in n:
    y.append(f(t))

plt.plot(n, y)
plt.show()

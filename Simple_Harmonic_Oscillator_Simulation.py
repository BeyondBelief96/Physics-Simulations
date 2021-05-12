# Mass-Spring Damped System Euler-Method Numerical Solution
# Author: Brandon Berisford
# Github: https://github.com/BeyondBelief96

import numpy as np
from matplotlib import pyplot as plt
from numpy.linalg import inv


# variables
m = 2.0  # mass of block on spring
k = 2.0  # spring constant
c = 1.0  # damping constant (Critical Damping = 2*SQRT(m*k))
F0 = 1.0  # Amplitude of Forcing Function (Set to 0.0 for no forcing term)

# time-step interval (Try using dt = 0.1. This Euler Method Integrator fails for dt too big.)
# If dt is too big, your results with no damping term will grow to infinity, which is not what we
# know to be true.
dt = 0.001
omega = 1.0  # angular velocity
time = np.arange(0.0, 40.0, dt)  # array of each time step

# initial state
y = np.array([0, 0])  # Initial State Vector [Velocity, Displacement]
A = np.array([[m, 0.0], [0.0, 1.0]])  # A matrix
B = np.array([[c, k], [-1.0, 0.0]])  # B Matrix
F = np.array([0.0, 0.0])  # Forcing Term Vector

Y = []  # Array to store values for y after each time-step
force = []  # Array to store values for force after each time step


# time-stepping solution
for t in time:

    if(t <= 15):
        F[0] = F0*np.cos(omega*t)  # Calculate the force
    else:
        F[0] = 0.0
    y = y + dt*inv(A).dot(F - B.dot(y))  # Calculate the displacement
    Y.append(y[1])
    force.append(F[0])

    KE = 0.5*m*y[0]**2
    PE = 0.5*k*y[1]**2

    if t % 1 <= 0.01:
        print('Energy:', KE + PE)

# plot the results
t = [i for i in time]

plt.plot(t, Y)
plt.plot(t, force)
plt.title('Forced/Damped Harmonic Oscillator (Displacement/Force vs Time')
plt.grid(True)
plt.legend(['Displacement', 'Force'], loc='lower right')
print('Critical Damping: ', np.sqrt((-c**2.0 + 4.0*m*k) / (2.0*m)))
print('Natural Frequency: ', np.sqrt(k/m))
plt.show()

# Mass-Spring Damped System Runga Kutta 4th Order Numerical Solution
# Author: Brandon Berisford
# Github: https://github.com/BeyondBelief96

import numpy as np
from matplotlib import pyplot as plt
from numpy.linalg import inv


# Defining Forcing Function
def F(t):
    F = np.array([0.0, 0.0])  # Forcing Term Vector
    if(t <= 15):
        F[0] = F0*np.cos(omega*t)  # Calculate the force
    else:
        F[0] = 0.0

    return F


# G = derivative of y at time t.
def G(y, t):
    return A_inv.dot(F(t) - B.dot(y))


# Runga-Kutta 4th Order Algorithm
def RK4_step(y, t, dt):
    k1 = G(y, t)
    k2 = G(y + 0.5*k1*dt, t + 0.5*dt)
    k3 = G(y + 0.5*k2*dt, t + 0.5*dt)
    k4 = G(y+k3*dt, t + dt)
    return dt * (k1 + 2*k2 + 2*k3 + k4) / 6
    # return dt * G(y, t) #1st order integrator commented out. You can uncomment to compare accuracy


# variables
m = 2.0  # mass of block on spring
k = 2.0  # spring constant
c = 0.0  # damping constant (Critical Damping = 2*SQRT(m*k))
F0 = 0.0  # Amplitude of Forcing Function (Set to 0.0 for no forcing term)

# time-step interval (Try using dt = 0.1. This Euler Method Integrator fails for dt too big.)
# If dt is too big, your results with no damping term will grow to infinity, which is not what we
# know to be true.
dt = 0.1
omega = 1.0  # angular velocity
time = np.arange(0.0, 40.0, dt)  # array of each time step

# initial state
y = np.array([0, 1])  # Initial State Vector [Velocity, Displacement]
A = np.array([[m, 0.0], [0.0, 1.0]])  # A matrix
A_inv = inv(A)
B = np.array([[c, k], [-1.0, 0.0]])  # B Matrix
Y = []  # Array to store values for y after each time-step
force = []  # Array to store values for force after each time step


# time-stepping solution
for t in time:
    y = y + RK4_step(y, t, dt)
    Y.append(y[1])
    force.append(F(t)[0])

    KE = 0.5*m*y[0]**2
    PE = 0.5*k*y[1]**2

    if t % 1 <= 0.01:
        print('Energy:', KE + PE)

# plot the results
plt.plot(time, Y)
plt.plot(time, force)
plt.title('Forced/Damped Harmonic Oscillator (Displacement/Force vs Time')
plt.grid(True)
plt.legend(['Displacement', 'Force'], loc='lower right')
print('Critical Damping: ', np.sqrt((-c**2.0 + 4.0*m*k) / (2.0*m)))
print('Natural Frequency: ', np.sqrt(k/m))
plt.show()

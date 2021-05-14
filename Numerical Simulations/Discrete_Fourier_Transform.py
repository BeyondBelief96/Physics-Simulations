import numpy as np
from matplotlib import pyplot as plt

# Function is a peicewise function: |x| < 1 = x, |x| > 1 = 0

N = 100  # number of points
x = np.linspace(-2, 2, N)  # creating array of N x-points
y = np.zeros(N)  # creating array of N y points
# populating y array to match our function definition above
y[abs(x) < 1] = x[abs(x) < 1]


plt.plot(x, y)
plt.show()

c = np.zeros(N, complex)  # DFT Coefficients
n = np.arange(N)
for k in range(N):
    c[k] = np.sum(y*np.exp(-2j*np.pi*k*n/N))

plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(np.imag(c), label='imag')
plt.plot(np.real(c), label='real')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(abs(c), 'r', label='magnitude')
plt.legend()

plt.show()

# inverse discrete fourier transform

y2 = np.zeros(N, complex)
k = np.arange(N)

for n in range(N):
    y2[n] = 1/N*np.sum(c*np.exp(2j*np.pi*k*n/N))

plt.plot(y, "k.", label="original")
plt.plot(np.real(y2), label='recovered function')
plt.legend()
plt.show()

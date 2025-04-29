import time
import numpy as np
f = np.linspace(-1, 1, 100)
w = 2 * np.pi * f 
z = np.exp(1j*w)
M = 20

start = time.time()
z_wander = np.vander(z, M, increasing = True); Hz = 1/M * np.sum(z_wander, axis = 1)
end = time.time()
print(end - start)


start = time.time()
Hz1 = lambda N, z : np.sum(np.array([1/N * (z ** (-i)) for i in range(N)]), axis = 0); Hz1(20, z)
end = time.time()
print(end - start)


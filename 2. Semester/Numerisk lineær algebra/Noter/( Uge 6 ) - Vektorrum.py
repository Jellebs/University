import numpy as np 
import matplotlib.pyplot as plt


w = 2 + 1j 
z = 2 - 1j

# Lineær ligning system med komplekse tal

a = np.array([[1.0j, 2.0], 
              [2.0, 1.0-1.0j]])
b = np.array([3.0, -2.0 + 1.0j]) [:, np.newaxis]

aub = np.hstack([a, b])
aub[0, :] *= 1 /1.0j 
aub[1, :] += -(2*aub[0, :])
aub[1, :] *= 1/(1.+3j)
aub[0, :] += 2j * aub[1,:]
print(aub)

løsning = aub[:, 2]
print(løsning)
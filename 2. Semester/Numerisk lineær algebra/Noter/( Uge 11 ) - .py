import numpy as np
import matplotlib.pyplot as plt 

b0 = np.array([500_000, 700_000]) [:, np.newaxis] # Antal i by, antal i land.

a = np.array([
    [0.98, 0.03],
    [0.02, 0.97]
    ]) # Procent af dem der smutter til byen / bliver på landet og omvendt. 
b = b0
'''
for i in range(5): 
    print(f'b{i} = {b}')
    b = a @ b 
'''
x = np.empty(100)
y = np.empty(100)
fig, ax = plt.subplots()

for i in range(100): 
    x[i] = b[0, 0]
    y[i] = b[1, 0]
    b = a @ b 
    
ax.plot(x, 'o', label ="Landbefolkning")
ax.plot(y, 'o', label ="By befolkning")
# Eksempel :

# Ny basis w0 = (3,2), w1 = (1, -1)
# Koordinatsskiftmatrix
t = np.array([[3, 1], [2, -1]], dtype = float)

#effekten af A i den nye basis er
c = np.linalg.inv(t) @ a @ t

# Grænse befolkninger 
g = t @ np.array([[1, 0], [0, 0]]) @ np.linalg.inv(t) @ b0
print(g)

ax.legend()

F = np.array([[0, 1], [-1, 0]])

import matplotlib.pyplot as plt
import numpy as np 

v = np.array([[  66,   54,   56,   61,   56,   63], 
              [1.78, 1.54, 1.63, 1.72, 1.52, 1.76]])

fig, ax = plt.subplots()
ax.plot(*v, 'o')

print(np.mean(v[0, :]))
print(np.mean(v[1, :]))
# == 
print(np.mean(v, axis= 1)) # 1 = rækker, 0 = søjler.
print(np.mean(v, axis= 1, keepdims=True)) # Beholder dimensionen. 

v_mean = np.mean(v, axis= 1, keepdims=True)
w = v - v_mean

# kovariansmatricen. 

m, n = w.shape
c = (1 / (n-1)) * w @ w.T

# w = UZigmaVT 
# wwT = UZigmaVT (UZigmaVT)T 
# wwT = UZigmaVT VZigmaTUT
# wwT = UZigma In ZigmaTUT
# wwT = UZigmaZigmaT(ZigmaZigmaT er sigma_i^2 )UT 
# wwT har egenværdierne Sigma_i^2

u, s, _ = np.linalg.svd(w, full_matrices=False)
# varians 
# print((s * s) * 1/(n - 1))
# ax.set_ylim(-.5, .5)
# ax.plot(*(u.T @ w), 'o') # uT*W = VTZigma

ax.plot(*(u[:, [0]]) * np.linspace(-7, 5, 2) + v_mean) # Ligner lidt least square
# Skulle være ortogonal på: 
ax.plot(*(u[:, [1]] * np.linspace(-.1, .1, 2) + v_mean))
# Men aspect ratioen er ikke ens, så det ligner det ikke.

# Skaleringsfaktor: 
skalering = np.sqrt(np.diag(c))[:, np.newaxis]
w_ny = w / skalering

c_ny = (1/(n - 1)) * w_ny @ w_ny.T
u_ny, s_ny, _ = np.linalg.svd(c_ny, full_matrices =False) 
# Samme værdier, men det næste ser anderledes ud end Andrews

fig, ax = plt.subplots()
# ax.set_aspect("equal")
# ax.plot(*(u_ny.T @ w_ny, 'o')) # VTnyZigmaNy - # 

ax.plot(*v, 'o')
ax.plot(*(u_ny * skalering)[:, 0] * np.linspace(-2, 2, 2), + v_mean)
ax.plot(*(u_ny * skalering)[:, 1] * np.linspace(-.1, .1, 2), + v_mean)

# Hvis egenværdier er forskellige af hinanden, så er egenvektorerne lineært uafhængige. Da er matricen diagonaliserbar.
# Der gælder dog, at hvis A in 3x3 så skal den have 3 egenværdier. Hvis A er symmetrisk er dette dog en undtagelse, og da vil A være diagonaliserbar med 2 egenværdier. 

s = 1e-9 
a = np.array([[1.0, 1.0], 
              [  s, 0.0],
              [0.0,   s]])

egenvaerdier = np.linalg.eigvals(a.T@a)
singv = np.linalg.svd(a, compute_uv=False)
print(np.allclose(singv, [np.sqrt(2+s**2), s])) # == True

egenvaerdier = np.linalg.eigvals(a @ a.T)
print(egenvaerdier)

# plt.show()  



from sympy import *
import numpy as np
import matplotlib.pyplot as plt

w = np.linspace(-10, 10, 100)
def setup(ax): 
    ax[0].set_ylabel("$|X(e^{jw})|$"); ax[1].set_ylabel("$\\angle X(e^{jw})$")
    ax[0].grid(True); ax[1].grid(True)
    

fig, ax = plt.subplots(2, 1, sharex= True)
Hjw = (1 + np.exp(-1j*w))/(2*1j*w + 5)
magnitude = np.abs(Hjw)
phase = np.angle(Hjw)
setup(ax)
ax[0].plot(w, magnitude, label = "$X(e^{jw})$") 
ax[1].plot(w, phase) 

plt.show()

w = np.linspace(-2*np.pi, 2*np.pi, 100)
fig, ax = plt.subplots(2, 1, sharex= True)
Hejw = 1 - np.exp(-1j*w)/2
magnitude = np.abs(Hejw)
phase = np.angle(Hejw)
setup(ax)
ax[0].plot(w, magnitude, label = "$X(e^{jw})$") 
ax[1].plot(w, phase) 
plt.show()

w = np.linspace(-2*np.pi, 2*np.pi, 100)
fig, ax = plt.subplots()
Hejw = (1 - np.exp(-2j*w))/(1j*w) 
magnitude = np.abs(Hejw)

ax.set_ylabel("$|X(e^{jw})|$")
ax.grid(True)
ax.plot(w, magnitude, label = "$X(e^{jw})$") 
 
plt.show()




fig, ax = plt.subplots()
t = np.linspace(-2, 2, 50)
yt = (t**3)/3 
ax.grid(True)
ax.plot(t, yt, label = "yt") 
plt.show()

fig, ax = plt.subplots()
n = np.linspace(0, 5, 6, dtype=np.int64)
print(n)
yn = (1/2) *( n**2 + n )
ax.stem(n, yn, label = "yn")
plt.show()


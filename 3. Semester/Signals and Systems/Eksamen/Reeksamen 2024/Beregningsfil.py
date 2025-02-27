from sympy import * 
import numpy as np
import matplotlib.pyplot as plt

def bodeplot(Hjw, w): 
    fig, ax = plt.subplots(2, 1, sharex= True)
    ax[0].set_ylabel("$|X(e^{jw})|$"); ax[1].set_ylabel("$\\angle X(e^{jw})$")
    ax[0].grid(True); ax[1].grid(True)
    magnitude = np.abs(Hjw)
    phase = np.angle(Hjw)
    ax[0].plot(w, magnitude, label = "$X(e^{jw})$") 
    ax[1].plot(w, phase)
    plt.show()
    return fig, ax 

# ? Opgave 2 
# * Kontinuer
fig, ax = plt.subplots(2, 1)
t = np.linspace(-2, 2, 50)
h = np.array([5**i if i > 0 else 0 for i in t])
x = np.array([1 if i > 0 else 0 for i in t])
ax[0].plot(t, x, label = "x(t)")
ax[1].plot(t, h, label = "h(t)", color = "orange")
fig.legend()
plt.show()

fig, ax = plt.subplots()
y = -1 + np.exp(t)
ax.plot(t, y, label = "y(t)")
fig.legend()
plt.show()

# * Diskrete 
n = np.linspace(-2, 3, 6, dtype=np.int64)
h = np.array([3**i if i > 0 else 0 for i in n])
x = np.array([2**i if i > 0 else 0 for i in n])
fig, ax = plt.subplots(2)
ax[0].stem(n, h, linefmt='tab:blue', label='h[n]')
ax[1].stem(n, x, linefmt='tab:orange', label='x[n]')
fig.legend()
plt.show()


fig, ax = plt.subplots()
n = np.linspace(-2, 3, 6)
y = np.array([(2**i) * (1.5**(i+1)) - 2*(2**i) for i in n])
ax.stem(n, y, linefmt='tab:blue', label='h[n]')
plt.show()



# ? Opgave 4
w = np.linspace(-10, 10, 100) 
Hjw = (1j*w  + 1)/(2j*w + 5)
bodeplot(Hjw, w)

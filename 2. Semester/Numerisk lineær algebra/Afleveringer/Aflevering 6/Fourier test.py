import numpy as np
import matplotlib.pyplot as plt

x, h = np.linspace(0, np.pi, 100, retstep= True)
f = x**3
konstant = np.ones_like(x)

def indre_produkt(f, g, h): 
    return np.trapz(f*g, dx=h)

fig, ax = plt.subplots()
ax.plot(x, konstant)
ax.plot(x, f)

print(f * konstant)
def norm_sq(f, h): 
    return indre_produkt(f, f, h) 

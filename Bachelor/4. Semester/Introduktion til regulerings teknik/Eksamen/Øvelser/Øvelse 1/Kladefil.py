import matplotlib.pyplot as plt
import numpy as np
from sympy import *



def bodeplot(G, s, poler): 
    
    fig, ax = plt.subplots()
    ax.plot(s, G)
    ax.set_ylabel("Amplitude")
    ax.set_xlabel("Tid(s)")

    # Fremhæv poler. 
    index = [np.where(abs(s - poler[i]) < 0.1 ) for i in range(len(poler))]
    try: 
        for i in index: 
            ax.plot(s[i], G[i], marker = "X", label = "Pol")
    except: 
        print("Fejlede med at plotte alle poler.")
    fig.legend()
    plt.show()

def ekstraOpgave():
    s = np.logspace(0, 2, 1000)
    G = 50000/((s + 50)*(s + 1000))
    bodeplot(G, s, [50, 1000])

# Prøvede at lade sympy lave transformationen. 
# exponent = exp(-t/TC)*ut(t)
# eq_t = convolution(Heaviside(t), exponent)
# eq_s = laplace_transform(eq_t, t, s)


TC = 20e-3
t, s, k= symbols("t, s, k")
t_num = np.linspace(-2, 2, 100)
# ut = lambda t: (t > 0).astype(float) + (t==0).astype(float)

alpha = 50
eq_t = inverse_laplace_transform(k * 1/(s + alpha), s, t)
pprint(eq_t)



s = np.linspace(0.01, 100, 100)
K = 1 
G = K * 1/(s**2 + alpha * s) 
fig, ax = plt.subplots()
ax.plot(s, G, label = "Transfer function")
fig.legend()
plt.show()
import numpy as np
from Uni.Vaerktoejer import visOpgave
from Uni.Formelsamling.SignalerOgSystemer import kontinuertTidsFourierSerie as CTFS 
import matplotlib.pyplot as plt

# visOpgave("Opgaveregning/Eksempel 3.5.png")

T = 2*np.pi # Arbitræer interval, men 2π er et godt udgangspunkt for et interval
omega0 = 2*np.pi/T
T1 = 1/4 * T 

# function
x = lambda t, t0: (np.abs(t) < t0).astype(float) # Binært tjek, hvis Ja = True, nej = False. 
# Det bliver lavet til type float(0, 1)
# Hvis værdien var mere end 1, så kunne jeg gange en skalar på. 

# time steps

tInt = np.linspace(-T/2, T/2, 100)
xt = x(tInt, T1)
antalKoefficienter = [1, 2, 3, 8, 12, 15, 20, 25, 30, 50] 

def ak_fun(k):     # Udledt ud fra the synthesis equation
    if k == 0: return 1/2
    return np.sin(k*np.pi/2)/(k*np.pi)

'''
x_hat = lambda t, K, omega0, ak: sum(ak(k)*np.exp(1j*k*omega0*t) for k in range(-K, K + 1))   # The analysis equation 
# Matematisk siger vi at estimationen går mod signalet når antallet af koefficienter går mod uendelig. 
# Her tester jeg estimationerne ud fra

x_approksimationer = {} # Skal være et bibliotek: x_k = ...
for antal in antalKoefficienter: 
    x_approksimationer[antal] = np.real(x_hat(tInt, antal, omega0, ak_fun)) 


for i in range(max(x_approksimationer.keys())):
    print([i*omega0, - i*omega0])
    print(ak_fun(i), ak_fun(-i))
    print("\n")
    # data = [i*omega0, -i*omega0,], [ak_fun(i), ak_fun(-i)]


fig, ax = plt.subplots(nrows=2, figsize=(16, 8))


for i in range(max(x_approksimationer.keys())):
    ax[0].set_title('ak coefficients')
    ax[0].stem([-i*omega0, i*omega0,], [ak_fun(i), ak_fun(-i)])

ax[1].plot(tInt, xt, label='x[t]', linewidth=3)
for i in x_approksimationer:
    ax[1].plot(tInt, np.real(x_approksimationer[i]), ':',
            label=f'{i} Fourier coeff.s', alpha=0.75)

ax[1].legend()
plt.show()
'''








# Hele opskriften har jeg koget ned til nogle funktioner som sørger for det hele for mig: 

ctfs = CTFS() # Kontinuert tids fourier serie
koefficienter = ctfs.findKoefficienter(ak_fun, max(antalKoefficienter))
# 
xt = lambda t, T1: (np.abs(t) < T1).astype(float) # 0 hvis udenfor intervallet, 1 hvis indenfor
xt = xt(tInt, T1)
x_approx = ctfs.approksimer(xt, tInt, antalKoefficienter, omega0, ak_fun)
ctfs.plot(koefficienter)
ctfs.plot(x_approksimationer = x_approx, xt = xt, tInt = tInt)
ctfs.plot(koefficienter, xt = xt, x_approksimationer = x_approx, tInt = tInt)
# print(len(x_approx))


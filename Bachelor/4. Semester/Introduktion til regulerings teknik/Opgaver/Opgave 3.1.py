from scipy.signal import * 
import control as ct
import matplotlib.pyplot as plt
import numpy as np
import Uni.Vaerktoejer.Links as links

def plotInputOutput(t, rt, output = "Output"):
    s = ct.tf('s')
    Gs = 500 * ((s + 8) * (s + 10) * (s + 15)) / (s*(s+38)*(s**2 + 2*s + 25))
    # T, yout = ct.step_response(Gs) # 1*u(t)
    T_Cs, Cs = ct.forced_response(Gs, t, rt) # y = Gs * r(t) 
    T_Es, Es = ct.feedback(Cs, rt)
    fig, ax = plt.subplots()
    print(Gs)
    ax.plot(t, rt, label = "Input signal")
    ax.plot(T_Es, Es, label = output)
    fig.legend()
    plt.show()

t = np.linspace(-10, 50, 100)
rt = 37 * t * (t>= 0).astype(float)
# plotInputOutput(t, rt, "r(t) = 37t*u(t)")

A, p, C = residuez([1, 4], [10])

print(A)
print(p)
print(C)

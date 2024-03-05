#   _______     ___             _______      ________    _____   ____
#  |        \    |             /       \    /        \     |    __/  
#  |        /    |            |         |  |               | __/     
#  |--------     |            |         |  |               |/\__     
#  |        \    |       ___  |         |  |               |   \__   
#  |_______ /     \_______/    \_______/    \________/   __|__  __\__

#   ________    ____________      ___        _______        _______           ___       ____    ____    ____    ____    __________     _______     
#  |        \         |          /   \      /              |        \        /   \       | \    / |      | \    / |    |              |        \   
#  |         |        |         |     |    |               |        |       |     |      |  \  /  |      |  \  /  |    |              |        |   
#  |         |        |         /-----\    |      ____     |________/       /-----\      |   \/   |      |   \/   |    |------        |________/   
#  |         |        |        |       |   |          |    |        \      |       |     |        |      |        |    |              |        \   
#  |________/   ______|_____  _|_     _|_   \________/   __|__       \__  _|_     _|_  __|__    __|__  __|__    __|__  |__________  __|__       \__

import matplotlib.pyplot as plt 
import numpy as np
import control as ct

class opgaveHjælp: 
    def __init__(self) -> None:
        print("Initialized")

    def __plot(self, ax, x, y, funktionLabel, xlabel = "", ylabel = "", colors = "", limits = ""): 
        def __setLimits(): 
            x_lim = limits[0, :]
            y_lim = limits[1, :]
            ax.set_xlim(limits[0, :]); ax.set_ylim(limits[1, :]); ax.hlines([0], x_lim[0], x_lim[1], "black"); ax.vlines([0], y_lim[0], y_lim[1], "black")

        ax.set_xlabel = xlabel
        ax.set_ylabel = ylabel
        if type(limits) != str: 
            __setLimits()
        else: 
            ax.hlines(0, -2, 10, "black"); ax.vlines(0, -5, 30, "black")
        c = next(colors)["color"] if type(colors) != str else "blue"
        ax.plot(x, y, label = funktionLabel, color = c)
        ax.grid(True)

    def plot(self, x, y, signalLabel, limits = "", save = False): 
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        colors = plt.rcParams["axes.prop_cycle"]() # Liste med de næste farver som matplotlib har klar til en
        for i in range(len(x.shape)): 
            if len(x.shape) == 1: self.__plot(ax, x, y, signalLabel, "Tid", "Amplitude", limits = limits); break
            self.__plot(ax, x[:, i], y[:, i], signalLabel, "Tid", "Amplitude",  colors = colors, limits = limits) 
        fig.legend()
        if save == True: fig.savefig("Plot.pdf")
        plt.show()
    # Eksempel med et tilbagekoblet system med regulatoren K og processen G(s) = 1/s * 1/(s+5)

hjaelper = opgaveHjælp()
K = 17.4
num = [K] # 0s^2 + 0s + K  
den = [1, 5, K] # G1 * G2 = s^2 +5s + K 
Gcl = ct.tf(num, den)

T = [0.2, 6]
s = np.linspace(T[0], T[1], 100)
G3 = 17.4/(s**2 + 5*s)

Gcl = ct.feedback(Gcl, 1)

_, Gcl = ct.step_response(Gcl, s)

hjaelper.plot(s, Gcl, "Transfer funktion", np.array([[0.2, 6], [0, 1.5]]), True)





# ------------------------------------------------------------------------ #




diagram()
    # scope.savefig()  # save scope figure as scope0.pdf, need to set hold=False



